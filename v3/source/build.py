import re
V='/home/claude/jovie/v3/site/'
src=open(V+'src.html').read()
WEBHOOK=re.search(r"https://services\.leadconnectorhq\.com/hooks/[^'\"]+",open('/home/claude/jovie/repo/public/index.html').read()).group(0)
def inner(name):
    s=open(V+'assets/'+name).read()
    vb=re.search(r'viewBox="([^"]+)"',s).group(1)
    body=re.search(r'<svg[^>]*>(.*)</svg>',s,re.S).group(1)
    body=re.sub(r'\sfill="#[0-9A-Fa-f]{6}"','',body)
    return vb,body.strip()
SYM_VB,SYM=inner('symbol.svg'); LOGO_VB,LOGO=inner('logo-h.svg')
SYM0='0 0 '+' '.join(SYM_VB.split()[2:])

LOOP={'hero':False,'arrive':True,'starter':True,'preparation':False,'share':True,'dessert':True,'stay':True}
def scene(name,desc,id_attr='',lazy=True):
    lz=' loading="lazy"' if lazy else ''
    lp=' loop' if LOOP[name] else ''
    return (f'<div class="scene"{id_attr}>'
            f'<picture><source media="(max-width:699px)" srcset="assets/v/{name}-m.webp"><img src="assets/v/{name}-d.webp" alt="" data-poster width="1600" height="900" decoding="async"{lz}></picture>'
            f'<video muted playsinline{lp} preload="none" aria-hidden="true" data-d="assets/v/{name}-d" data-m="assets/v/{name}-m"></video>'
            f'<p class="sr">{desc}</p></div>')

R=[('01','Arrive','arrive','The lobby','Come in and be welcome','A warm hello under the terracotta arches and a cold mint lemonade while the table is set',['Mint lemonade'],'The JOVIE lobby with terracotta arches and the brass sign behind the reception desk','Mint lemonade'),
   ('02','Starter','starter','The dining hall','It starts with bread','Hummus and mezze beside the botanical mural with bread straight from the oven',['Hummus','Mezze platter','Bread from the oven'],'The dining hall at evening with a hand painted botanical mural and glowing rattan lamps','Hummus and bread'),
   ('03','Preparation','preparation','The wood-fire kitchen','Good things take time','Pizza from the wood-fire oven and grills cooked slowly over olive wood',['Wood-fired Margherita','Beef pepper steak','Shish tawook','Lamb chops'],'A cook slides bread into the copper wood-fire oven at evening','Beef pepper steak'),
   ('04','Share','share','The family table','Better together','Platters for the middle of the table · everyone tastes everything',['Mixed grill platter','Pizza for the table','Fettuccine Alfredo'],'The private dining room with one long table under a curved timber ceiling','The mixed grill platter'),
   ('05','Dessert','dessert','The juice bar','End on something sweet','Kunafa · tiramisu and a molten lava cake with fresh juice under the great arch',['Kunafa','Tiramisu','Molten lava cake'],'The juice bar under a great terracotta arch with fresh juices · fruit and cakes','Kunafa'),
   ('06','Stay','stay','The terrace','Stay a little longer','Cappuccino and tea under the lanterns · nobody rushes the table',['Cappuccino','Tea'],'The JOVIE terrace at blue hour with rattan lanterns and the sea beyond','Cappuccino and tea')]
PALT={'arrive':'A tall glass of mint lemonade in a terracotta arch niche','starter':'Hummus and warm bread in a terracotta arch niche','preparation':'Sliced beef pepper steak with the wood-fire oven glowing behind','share':'Hands sharing a mixed grill platter · pizza · fettuccine and hummus','dessert':'Kunafa with pistachio and a stretch of melted cheese','stay':'A cappuccino and a glass cup of tea in a terracotta arch niche'}
rooms=[];flick=[];board=[]
prev='hero'
for i,(n,name,key,where,line,body,dishes,alt,cap) in enumerate(R):
    rooms.append(f'''    <article class="room" id="r-{key}" aria-labelledby="t-{key}"{' data-z0="1.22"' if key=="share" else ""}>
      <div class="stick">
        <div class="prev" aria-hidden="true" data-d="assets/v/{prev}-d.webp" data-m="assets/v/{prev}-m.webp"></div>
        <div class="num" aria-hidden="true"><span class="lab">Ritual {n} · {where}</span><b>{n}</b><span class="nm">{name}</span></div>
        {scene(key,alt)}
        <p class="tag lab" aria-hidden="true">Ritual {n} / 06</p>
        <div class="copy wrap">
          <div><p class="lab">Ritual {n} · {where}</p><h3 class="disp" id="t-{key}" tabindex="-1">{name}</h3><p class="line">{line}</p><p class="body">{body}</p></div>
          <figure class="inset"><div class="arch"><img src="assets/img/p-{key}.webp" alt="{PALT[key]}" width="600" height="860" loading="lazy" decoding="async"></div><figcaption>{cap}</figcaption></figure>
        </div>
      </div>
    </article>''')
    prev=key
    flick.append(f'    <a href="#r-{key}" data-name="{name}" aria-label="Ritual {n} · {name}"><svg viewBox="{SYM0}" aria-hidden="true"><use href="#sym"/></svg></a>' + ('\n    <span class="bar" aria-hidden="true"></span>' if i==2 else ''))
    pd=''.join(f'<li>{d}</li>' for d in dishes)
    board.append(f'      <li class="rv"><a href="#r-{key}" data-room="{i}"><svg class="ic" viewBox="{SYM0}" aria-hidden="true"><use href="#sym"/></svg><span class="lab">Ritual {n}</span><h3>{name}</h3></a><ul>{pd}</ul></li>')

GUESTS=''.join(f'<option value="{g}"{" selected" if g==2 else ""}>{g} {"guest" if g==1 else "guests"}</option>' for g in range(1,13))+'<option value="13+">13 or more</option>'
times=[]
for m in range(12*60,23*60+1,30):
    h,mm=divmod(m,60);h12=12 if h%12==0 else h%12
    times.append(f'<option value="{h:02d}:{mm:02d}"{" selected" if m==20*60 else ""}>{h12}:{mm:02d} pm</option>')
OCC=[('Dinner','Dinner'),('Family gathering','Family gathering'),('Birthday','Birthday'),('Private dining','Private dining'),('Business','Business')]
occ=''.join(f'<label><input type="radio" name="occasion" value="{v}"{" checked" if i==0 else ""}><span>{t}</span></label>' for i,(v,t) in enumerate(OCC))
SEAT=[('Any table','Any table'),('Dining hall','Dining hall'),('Terrace','Terrace'),('Private room','Private room')]
seat=''.join(f'<option value="{v}">{t}</option>' for v,t in SEAT)
rep={'SYM_VB':SYM_VB,'SYM0':SYM0,'SYM':SYM,'LOGO_VB':LOGO_VB,'LOGO':LOGO,'WORD_VB':'0 0 '+' '.join(LOGO_VB.split()[2:]),
     'ROOMS':'\n'.join(rooms),'FLICK':'\n'.join(flick),'BOARD':'\n'.join(board),'GUESTS':GUESTS,'TIMES':''.join(times),
     'OCC':occ,'SEAT':seat,'WEBHOOK':WEBHOOK,
     'HERO_SCENE':scene('hero','The JOVIE garden stair at dusk with a falling water wall and palms',' id="heroScene"',lazy=False),
     'LEAVES':re.search(r'<svg[^>]*>(.*)</svg>',open(V+'assets/leaves.svg').read(),re.S).group(1),
     'BASE':'https://wearemarketingbf-dotcom.github.io/jovie-website-v2/v3/'}
out=src
for k,v in rep.items(): out=out.replace('{{'+k+'}}',v)
left=re.findall(r'\{\{[A-Z_]+\}\}',out); assert not left,left
open(V+'index.html','w').write(out); print('ok',len(out))
