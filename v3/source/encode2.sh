#!/usr/bin/env bash
# usage: encode2.sh <name> <pingpong|once>
#   pingpong · forward then reverse · seamless loop with no ghosting
#   once     · plays one time and holds its last frame (clips with water or a person acting)
set -euo pipefail
N=$1; MODE=$2
IN=/home/claude/jovie/v3/hf/out/$N.mp4
OUT=/home/claude/jovie/v3/site/assets/v
TMP=/home/claude/jovie/v3/hf/tmp; mkdir -p $TMP $OUT
BASE="fps=24,scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,format=yuv420p"
ffmpeg -v error -y -i "$IN" -an -vf "$BASE" -c:v libx264 -preset veryfast -crf 12 $TMP/$N-base.mp4
F=$(ffprobe -v error -count_frames -select_streams v:0 -show_entries stream=nb_read_frames -of csv=p=0 $TMP/$N-base.mp4)
if [ "$MODE" = pingpong ]; then
  E=$((F-2))
  ffmpeg -v error -y -i $TMP/$N-base.mp4 -an -filter_complex \
   "[0:v]split[a][b];[b]reverse,trim=start_frame=1:end_frame=$E,setpts=PTS-STARTPTS[r];[a][r]concat=n=2:v=1:a=0[v]" \
   -map "[v]" -c:v libx264 -preset veryfast -crf 12 $TMP/$N-loop.mp4
else
  cp $TMP/$N-base.mp4 $TMP/$N-loop.mp4
fi
# desktop 1920x1080
ffmpeg -v error -y -i $TMP/$N-loop.mp4 -c:v libx264 -preset veryfast -crf 26 -profile:v high -pix_fmt yuv420p -movflags +faststart -an $OUT/$N-d.mp4
ffmpeg -v error -y -i $TMP/$N-loop.mp4 -c:v libvpx-vp9 -b:v 0 -crf 38 -row-mt 1 -deadline good -cpu-used 4 -an $OUT/$N-d.webm
# mobile portrait 540x960 (centre crop)
ffmpeg -v error -y -i $TMP/$N-loop.mp4 -vf "crop=608:1080:(iw-608)/2:0,scale=540:960:flags=lanczos" -c:v libx264 -preset veryfast -crf 26 -profile:v high -pix_fmt yuv420p -movflags +faststart -an $OUT/$N-m.mp4
ffmpeg -v error -y -i $TMP/$N-loop.mp4 -vf "crop=608:1080:(iw-608)/2:0,scale=540:960:flags=lanczos" -c:v libvpx-vp9 -b:v 0 -crf 38 -row-mt 1 -deadline good -cpu-used 4 -an $OUT/$N-m.webm
# posters = first frame
ffmpeg -v error -y -i $TMP/$N-loop.mp4 -frames:v 1 -vf scale=1600:900:flags=lanczos $TMP/$N-p.png
ffmpeg -v error -y -i $TMP/$N-loop.mp4 -frames:v 1 -vf "crop=608:1080:(iw-608)/2:0,scale=540:960:flags=lanczos" $TMP/$N-pm.png
python3 -c "from PIL import Image;Image.open('$TMP/$N-p.png').save('$OUT/$N-d.webp',quality=72,method=6);Image.open('$TMP/$N-pm.png').save('$OUT/$N-m.webp',quality=72,method=6)"
echo "$N $MODE frames=$F $(du -k $OUT/$N-d.webm | cut -f1)KB webm-d $(du -k $OUT/$N-m.webm | cut -f1)KB webm-m"
