#!/usr/bin/env bash
# usage: encode.sh <name>   (reads hf/out/<name>.mp4 · writes site/assets/v/<name>-{d,m}.{mp4,webm,webp})
set -euo pipefail
N=$1
IN=/home/claude/jovie/v3/hf/out/$N.mp4
OUT=/home/claude/jovie/v3/site/assets/v
TMP=/home/claude/jovie/v3/hf/tmp; mkdir -p $TMP $OUT
D=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$IN")
X=1.2                                    # crossfade seam length
L=$(python3 -c "print(round($D-$X,3))")  # loop length
O=$(python3 -c "print(round($D-2*$X,3))")
# seamless loop master (1080p, high quality intermediate)
ffmpeg -v error -y -i "$IN" -an -filter_complex \
 "[0:v]fps=24,scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,format=yuv420p,split[a][b];[a]trim=0:$X,setpts=PTS-STARTPTS[head];[b]trim=$X:$D,setpts=PTS-STARTPTS[body];[body][head]xfade=transition=fade:duration=$X:offset=$O[v]" \
 -map "[v]" -c:v libx264 -preset veryfast -crf 14 $TMP/$N-loop.mp4
# desktop 1280x720
ffmpeg -v error -y -i $TMP/$N-loop.mp4 -vf scale=1280:720:flags=lanczos -c:v libx264 -preset veryfast -crf 25 -profile:v high -pix_fmt yuv420p -movflags +faststart -an $OUT/$N-d.mp4
ffmpeg -v error -y -i $TMP/$N-loop.mp4 -vf scale=1280:720:flags=lanczos -c:v libvpx-vp9 -b:v 0 -crf 37 -row-mt 1 -deadline good -cpu-used 4 -an $OUT/$N-d.webm
# mobile portrait 540x960 (centre crop of the 1080p frame)
ffmpeg -v error -y -i $TMP/$N-loop.mp4 -vf "crop=608:1080:(iw-608)/2:0,scale=540:960:flags=lanczos" -c:v libx264 -preset veryfast -crf 26 -profile:v high -pix_fmt yuv420p -movflags +faststart -an $OUT/$N-m.mp4
ffmpeg -v error -y -i $TMP/$N-loop.mp4 -vf "crop=608:1080:(iw-608)/2:0,scale=540:960:flags=lanczos" -c:v libvpx-vp9 -b:v 0 -crf 38 -row-mt 1 -deadline good -cpu-used 4 -an $OUT/$N-m.webm
# posters = first frame of the loop
ffmpeg -v error -y -i $TMP/$N-loop.mp4 -frames:v 1 -vf scale=1600:900:flags=lanczos -q:v 2 $TMP/$N-p.png
ffmpeg -v error -y -i $TMP/$N-loop.mp4 -frames:v 1 -vf "crop=608:1080:(iw-608)/2:0,scale=540:960:flags=lanczos" $TMP/$N-pm.png
python3 -c "from PIL import Image;Image.open('$TMP/$N-p.png').save('$OUT/$N-d.webp',quality=72,method=6);Image.open('$TMP/$N-pm.png').save('$OUT/$N-m.webp',quality=72,method=6)"
ls -la $OUT/$N-* | awk '{print $5, $9}'
