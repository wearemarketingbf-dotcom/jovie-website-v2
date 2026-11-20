import re, math
from PIL import Image
V = '/home/claude/jovie/v2/'
src = open(V + 'src.html').read()
WEBHOOK = re.search(r"https://services\.leadconnectorhq\.com/hooks/[^'\"]+", open('/home/claude/jovie/repo/public/index.html').read()).group(0)

def inner(name):
    s = open(V + 'assets/' + name).read()
    vb = re.search(r'viewBox="([^"]+)"', s).group(1)
    body = re.search(r'<svg[^>]*>(.*)</svg>', s, re.S).group(1)
    body = re.sub(r'\sfill="#[0-9A-Fa-f]{6}"', '', body)
    return vb, body.strip()

def size(n):
    return Image.open(V + 'assets/' + n + '.webp').size

SYM_VB, SYM = inner('symbol.svg')
LOGO_VB, LOGO = inner('logo-h.svg')
TICKS = ''.join(f'<line class="tick" x1="{29+24*math.sin(a*math.pi/6):.2f}" y1="{29-24*math.cos(a*math.pi/6):.2f}" x2="{29+27*math.sin(a*math.pi/6):.2f}" y2="{29-27*math.cos(a*math.pi/6):.2f}"/>' for a in range(12))

R = [
 ('01', 'Arrive', 'The lobby', 'r-arrive', 'Come in and be welcome', 'A warm hello at the door<br>and a cold mint lemonade', 'A couple is welcomed by a host under the terracotta arches of the JOVIE lobby'),
 ('02', 'Starter', 'The dining hall', 'r-starter', 'It starts with bread', 'Hummus and mezze<br>with bread straight from the oven', 'Hands tear za’atar flatbread on a stone table'),
 ('03', 'Preparation', 'The wood-fire kitchen', 'r-preparation', 'Good things take time', 'Pizza from the wood-fire oven<br>and grills over olive wood', 'A copper wood-fire oven glows in the open kitchen'),
 ('04', 'Share', 'The private dining room', 'r-share', 'Better together', 'Platters for the middle of the table<br>everyone tastes everything', 'Plates passed across a long table in the private dining room'),
 ('05', 'Dessert', 'The juice bar', 'r-dessert', 'End on something sweet', 'Kunafa · tiramisu<br>and a molten lava cake', 'A pistachio dessert and fresh orange juice at the juice bar'),
 ('06', 'Stay', 'The outdoor deck', 'r-stay', 'Stay a little longer', 'Cappuccino and tea on the deck<br>nobody rushes the table', 'Mint tea glasses on a stone table on the outdoor deck'),
]
rit = []
for n, name, where, img, h, p, alt in R:
    w, hh = size(img)
    rit.append(f'''      <article class="rit" aria-label="Ritual {n} {name}">
        <div class="rit-txt">
          <span class="rit-num" aria-hidden="true">{n}</span>
          <h3 class="disp">{name}</h3>
          <p class="line">{h}</p>
          <p class="body">{p}</p>
          <p class="lab where">Ritual {n} · {where}</p>
        </div>
        <figure class="rit-img" style="margin:0"><img src="assets/{img}.webp" alt="{alt}" width="{w}" height="{hh}" loading="lazy" decoding="async"><figcaption>{where}</figcaption></figure>
      </article>''')

M = [
 ('Arrive', 'r-arrive', ['Mint lemonade']),
 ('Starter', 'r-starter', ['Hummus', 'Mezze platter', 'Bread from the oven']),
 ('Preparation', 'r-preparation', ['Wood-fired Margherita', 'Beef pepper steak', 'Shish tawook', 'Lamb chops']),
 ('Share', 'r-share', ['Mixed grill platter', 'Pizza for the table', 'Fettuccine Alfredo']),
 ('Dessert', 'r-dessert', ['Kunafa', 'Tiramisu', 'Molten lava cake']),
 ('Stay', 'r-stay', ['Cappuccino', 'Tea']),
]
menu = []
for i, (name, img, dishes) in enumerate(M):
    li = ''.join(f'<li class="dish" data-img="assets/{img}.webp">{d}</li>' for d in dishes)
    menu.append(f'    <li class="course rv"><p class="lab"><small>{name}</small>Ritual 0{i+1}</p><ul class="dishes">{li}</ul></li>')

ROOM_ORDER = 1
ROOM = [('t1', 'room-lobby', 'Lobby', 'Terracotta arches and the brass sign', 'The JOVIE lobby with terracotta arched walls and the brass logo behind the reception desk'),
        ('t2', 'room-dining', 'Dining hall', 'A tropical mural and rattan light', 'The dining hall with a tropical mural and rattan pendant lamps'),
        ('t3', 'room-private', 'Private dining', 'One long table for the family', 'The private dining room with one long table'),
        ('t5', 'room-deck', 'Outdoor deck', 'A water wall and warm lamps', 'The outdoor deck with tables beside a lit water wall'),
        ('t7', 'room-stair', 'Garden stair', 'Up through the green', 'A floating stair rising through a lit garden'),
        ('t6', 'room-terrace', 'The terrace', 'A timber canopy over the evening', 'The JOVIE terrace under a timber lattice canopy at night')]
room = []
for cls, img, t, d, alt in ROOM:
    w, h = size(img)
    room.append(f'    <figure class="tile {cls} clip"><img src="assets/{img}.webp" alt="{alt}" width="{w}" height="{h}" loading="lazy" decoding="async"><figcaption><b>{t}</b><span>{d}</span></figcaption></figure>')

GUESTS = ''.join(f'<option value="{g}"{" selected" if g == 2 else ""}>{g}</option>' for g in range(1, 13)) + '<option value="13+">13 or more</option>'
times = []
for m in range(12 * 60, 23 * 60 + 1, 30):
    h, mm = divmod(m, 60)
    h12 = 12 if h % 12 == 0 else h % 12
    times.append(f'<option value="{h:02d}:{mm:02d}"{" selected" if m == 20 * 60 else ""}>{h12}:{mm:02d} pm</option>')
OCC = [('Dinner', 'dinner'), ('Family gathering', 'a family gathering'), ('Birthday', 'a birthday'), ('Private dining', 'private dining'), ('Business', 'a business meal')]
SEAT = [('Any table', 'any corner'), ('Dining hall', 'the dining hall'), ('Outdoor deck', 'the outdoor deck'), ('Private room', 'the private room')]
opt = lambda L: ''.join(f'<option value="{v}">{t}</option>' for v, t in L)

DISH = [d for _, _, ds in M for d in ds]
BAND = ''.join(f'<span>{d}<svg><use href="#sym"/></svg></span>' for d in DISH[:8])
BAND2 = ''.join(f'<span>{d}<svg><use href="#sym"/></svg></span>' for d in DISH[8:] + ['Olive wood', 'Noon to midnight'])
rep = {'SYM_VB': SYM_VB, 'SYM': SYM, 'LOGO_VB': LOGO_VB, 'LOGO': LOGO, 'WORD_VB': '0 0 ' + ' '.join(LOGO_VB.split()[2:]), 'TICKS': TICKS,
       'RITUALS': '\n'.join(rit), 'MENU': '\n'.join(menu), 'ROOM': '\n'.join(room), 'GUESTS': GUESTS,
       'BAND': BAND, 'BAND2': BAND2,
       'TIMES': ''.join(times), 'OCC': opt(OCC), 'SEAT': opt(SEAT), 'WEBHOOK': WEBHOOK}
out = src
for k, v in rep.items():
    out = out.replace('{{' + k + '}}', v)
left = re.findall(r'\{\{[A-Z_]+\}\}', out)
assert not left, left
open(V + 'index.html', 'w').write(out)
print('ok', len(out))
