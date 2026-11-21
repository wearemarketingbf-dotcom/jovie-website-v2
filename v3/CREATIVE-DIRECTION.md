# JOVIE website v3 · Through the arches

Creative direction · brand intelligence · storyboard · production plan · quality audit
Built with the Creative Experience Engine method (brief supplied by Karim · 21 Nov 2026)

---

## 01 · Brand intelligence

**Strategic DNA**
- JOVIE · Dining Rituals · Mediterranean wood-fire restaurant in Karachi for families and friends · premium casual
- Promise · *Joy made ritual* · "We do not serve dinner · we keep rituals"
- One evening is told as six locked rituals · Arrive · Starter · Preparation · Share · Dessert · Stay
- Business goal of the site · turn a visit into a table request (GoHighLevel webhook) · second goal · make the room feel real before the restaurant is photographed

**Visual DNA**
- Master shape is the **arch** (full semicircle top) · the guide calls it the *Echo arch* and extends it into architecture and signage
- Graphic grammar · Waves (dividers) · Echo arch (frames and crops) · Clay leaves (one cluster per artwork) · Space (negative space as a motif)
- Symbol · flame in an open circle · six ways to speak · open circle · brackets · bloom · supercrop · arc lattice · *flicker* (six flames in a row = six moments)
- Palette · terracotta #A26542 · olive #685C3F · sand #BC9D81 · deep brown #56351E · cream #F6F2EF · ink #231F20
- Type · Bellefair (display serif) · Source Sans 3 (text and tracked uppercase labels)

**Emotional DNA** · warm · unhurried · generous · Mediterranean light more than luxury gloss

**Motion DNA** · "Fire that takes its time" · slow, weighted, never bouncy · things open rather than slide · long ease-out curves · nothing flashes

**Spatial DNA** · the venue renders already are the brand world · terracotta arched lobby · botanical mural dining hall · copper wood-fire oven · private long table · juice bar under a great arch · rooftop terrace with rattan lanterns at blue hour

**Digital opportunity DNA**
- The arch can be the *camera* · every room is entered through an arch-shaped aperture that opens with scroll
- The flicker device can be the *progress bar* · six flames · the current ritual is lit
- Waves can be the section dividers · the open circle can be the cursor ring and the reserve button

**Brand constants** (never change) · logo files and lockups · six ritual names and order · palette · Bellefair + Source Sans 3 · copy without commas or full stops (" · " as separator) · no invented prices, reviews, awards, address or phone
**Creative variables** · camera language · arch aperture behaviour · section rhythm · which room carries which ritual

---

## 02 · Three creative directions

| | A · Through the arches | B · One table six moments | C · Fire that takes its time |
|---|---|---|---|
| Method | Spatial brand universe | Interactive product journey | Slow-time ember theatre |
| Metaphor | The evening is a walk through six rooms · every room opens through an arch | One overhead table fills course by course as you scroll | The wood fire narrates · the page cooks slowly |
| Hero | Dusk approach to the garden stair · a cinematic push-in · *Joy made ritual* | Empty set table from above · "your seat is set" | The oven mouth in the dark · flame symbol drawn in light |
| Signature scroll | Arch aperture grows from a small doorway to full bleed and reveals the next room in motion | Sticky top-down table · plates and hands arrive per ritual | Ember-lit typography · scenes revealed by firelight |
| AI assets | Seven image-to-video loops animated from the approved venue renders | Six consistent overhead table states + hand inserts | Fire macro loops · ember textures |
| Trade-offs | Strong brand fit · venue renders give stable start frames · videos are the heaviest asset so they must be lazy and paused off-screen | Very original but six consistent AI table states with hands and unconfirmed dishes is high artefact risk | Moody but drifts into the dark ember cliché and repeats the v1 fire sequence |

**Decision · A · Through the arches** with one idea borrowed from B (the menu is a single table of six round plates · the guide's own "One table six moments" spread). A uses the brand's master shape as the interaction itself, it is clearly different from v1 (editorial page) and v2 (noon to midnight sky and clock), and its AI production risk is the lowest because every clip starts from an approved render.

---

## 03 · Design system

- **Colour roles** · ground cream · text ink · display deep brown · accent terracotta · secondary olive · night sections deep brown with sand text
- **Type scale** · display Bellefair clamp(44px → 132px) line-height 1 · section titles clamp(34px → 72px) · body Source Sans 3 17–19px line-height 1.6 · labels 12px uppercase tracking .22em
- **Grid** · 12 columns · max 1440 · side gutter max(20px, 4vw) · mobile single column with 16px+ gutter and safe-area insets
- **Components** · arch frame (CSS clip-path inset round) · echo-arch outline (SVG concentric arches) · flicker nav (six flame buttons) · wave divider · open-circle button · arch reserve card
- **Motion tokens** · ease-open cubic-bezier(.22,1,.36,1) · ease-slow cubic-bezier(.65,0,.35,1) · reveal 900ms · stagger 80ms · aperture driven by scroll progress (no time duration) · hover 350ms
- **Reduced motion** · apertures render fully open · videos show posters only and never autoplay · no parallax · reveals appear instantly

---

## 04 · Scroll storyboard

| # | Section | Goal | Visual + motion | Asset | Mobile | Fallback |
|---|---|---|---|---|---|---|
| 0 | Hero · Arrive at dusk | Feel the place in three seconds | Full-bleed dusk loop · lockup and *Joy made ritual* · echo-arch outline draws once · scroll shrinks the scene back into an arch and the cream page rises | hero-garden loop | Same loop cropped centre · headline stacked | Poster image |
| 1 | Manifesto | Understand the idea | "A ritual is a small thing done with care…" four lines reveal one by one beside a small arch window | — | Lines stack | Static text |
| 2–7 | Six rooms · Arrive · Starter · Preparation · Share · Dessert · Stay | Discover · feel | Each room is a 200vh pinned stage · a small arch doorway in the centre grows to full bleed with scroll (clip-path inset round) while the clip inside scales 1.18 → 1 · then the ritual name, line and dishes rise in · the flicker nav lights that flame | One loop per room | Stage 160vh · text sits under the arch | Poster + text · arch fully open |
| 8 | One table · six moments | Understand the menu | Six round plates in an arc lattice · hover or tap a plate to read its ritual and dishes | Approved dish stills | 2 × 3 grid | Same |
| 9 | Reserve | Act | Arch-topped card · date · time · guests · occasion · seating · name · mobile · posts to GoHighLevel with source "jovie.pk website v3" | — | Full width card | Works without JS validation polish |
| 10 | Visit | Trust | Hours · Karachi · Instagram · big wordmark under a wave | — | Stacked | Same |

---

## 05 · Higgsfield production plan

**Workflow** · image-to-video · Kling 4.0 · 1080p · 6 s · 16:9 · start frame = approved JOVIE venue render (Preparation frame outpainted to 16:9 from the existing oven image)

**Production bible** (applies to every clip)
- Camera · slow gimbal dolly or push-in · 35mm · eye level · no shake · no zoom pulse
- Geometry · architecture must stay exactly as rendered · arches · signage · furniture never warp
- Life · only small natural motion · water · leaves · lamp glow · flames · glints
- Grade · warm terracotta and amber · film contrast · natural motion blur
- Negative · no people (except the cook in Preparation) · no birds · no text · no new objects · no cuts
- Web safe zone · the centre third carries the subject because every clip is seen through an arch

| Clip | Ritual / place | Start frame | Motion |
|---|---|---|---|
| hero | Arrive at dusk · garden stair | 01-garden-stair | dolly toward the floating stair · water curtain · palms |
| arrive | Arrive · lobby | 02-lobby | dolly between arches toward the brass sign |
| starter | Starter · dining hall | 04-dining-hall | dolly along banquette and mural · rattan lamps sway |
| preparation | Preparation · wood fire | r-preparation outpainted | push-in · flames · cook slides the bread |
| share | Share · private dining | room-private | push-in to the long table |
| dessert | Dessert · juice bar | 05-juice-bar | push-in under the great arch · glints on glass |
| stay | Stay · rooftop terrace | 07-rooftop-terrace | sideways drift · lanterns sway · sea shimmer |

**Delivery** · each clip → H.264 MP4 1280w (desktop) and 720w (mobile) + VP9 WebM · 1.2 s crossfade loop seam · WebP poster from frame 0 · `preload="none"` · plays only while its stage is on screen · paused otherwise · never autoplays under reduced motion

---

## Honesty notes
- Interiors are design renders and dishes are AI concept stills until the real shoot
- Clips are generated from those renders · they are not footage of the restaurant
- No address or phone is shown because neither is confirmed yet
