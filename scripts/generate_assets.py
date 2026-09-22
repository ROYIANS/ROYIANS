#!/usr/bin/env python3
"""Generate the original, dependency-free SVG artwork used in the profile."""
from html import escape
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / 'assets'
OUT.mkdir(exist_ok=True)
PALETTES = {
    'light': dict(paper='#f4f0e7', ink='#292c29', muted='#73756b', line='#d5d2c6', orange='#d85332', green='#576b50', blue='#476879', yellow='#edc963'),
    'dark': dict(paper='#202622', ink='#f0ecdf', muted='#b0b6a8', line='#414b42', orange='#f08460', green='#a9bd96', blue='#9fc0d0', yellow='#e5c777'),
}


def text(x, y, value, size=16, color='ink', family='sans', extra=''):
    fonts = {'sans': "'Trebuchet MS',Verdana,sans-serif", 'serif': "Georgia,'Times New Roman',serif", 'mono': "'Courier New',monospace"}
    return f'<text x="{x}" y="{y}" font-family="{fonts[family]}" font-size="{size}" fill="{P.get(color, color)}" {extra}>{escape(value)}</text>'


def line(x1, y1, x2, y2, color='line', width=1, extra=''):
    return f'<path d="M{x1} {y1}H{x2}" stroke="{P.get(color,color)}" stroke-width="{width}" {extra}/>' if y1 == y2 else f'<path d="M{x1} {y1}L{x2} {y2}" stroke="{P.get(color,color)}" stroke-width="{width}" {extra}/>'


def rect(x, y, w, h, color, extra=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{P.get(color,color)}" {extra}/>'


def circle(x, y, r, color, extra=''):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{P.get(color,color)}" {extra}/>'


def star(x, y, r, color='orange'):
    return f'<g transform="translate({x} {y})" fill="{P[color]}"><path d="M0 {-r}L{r*.23} {-r*.23}L{r} 0L{r*.23} {r*.23}L0 {r}L{-r*.23} {r*.23}L{-r} 0L{-r*.23} {-r*.23}Z"/></g>'


def svg(name, w, h, content, title):
    doc = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title>
<desc id="desc">Original geometric artwork for Joshua / ROYIANS. {escape(name)}.</desc>
{rect(0,0,w,h,'paper')}
{content}
</svg>
'''
    (OUT / f'{name}-{theme}.svg').write_text(doc)


def hero():
    c = rect(24,24,1152,512,'none',f'stroke="{P["line"]}"')
    c += text(58,70,'R /',28,extra='font-weight="700"')
    c += text(121,67,'ROYIANS',19,extra='letter-spacing="4"')
    c += text(1128,67,'JOSHUA  /  A PERSONAL WORKSHOP',14,'muted','mono','text-anchor="end"')
    c += line(58,94,1142,94)
    c += text(58,149,'CODE  /  CRAFT  /  EVERYDAY LIFE',15,'muted','mono')
    c += text(51,255,'Small ideas.',91,'ink','serif', 'letter-spacing="-5"')
    c += text(51,359,'Real things.',91,'ink','serif', 'letter-spacing="-5"')
    c += line(60,389,184,389,'orange',4)
    c += text(59,436,'Creative tools. Thoughtful little worlds.',22,'muted')
    # A small architectural world: an arch, a sun, a sheet, and a sound wave.
    c += '<g transform="translate(708 120)">'
    c += circle(212,159,150,'none',f'stroke="{P["line"]}" stroke-dasharray="3 9"')
    c += f'<path d="M82 302V134a118 118 0 0 1 236 0V302Z" fill="{P["green"]}"/>'
    c += f'<path d="M132 302V143a68 68 0 0 1 136 0V302Z" fill="{P["paper"]}"/>'
    c += circle(295,68,57,'orange')
    c += circle(295,68,43,'none',f'stroke="{P["paper"]}" stroke-opacity=".35"')
    c += '<g transform="translate(18 173) rotate(-12 83 67)">'
    c += rect(9,9,155,121,'ink') + rect(0,0,155,121,'paper',f'stroke="{P["ink"]}" stroke-width="2"')
    c += rect(15,17,35,35,'blue') + line(64,24,136,24,'ink',2) + line(64,37,122,37,'line',2)
    c += line(16,71,136,71,'ink',2) + line(16,87,136,87,'line',2) + line(16,103,91,103,'line',2) + '</g>'
    c += '<g transform="translate(237 238)">'
    c += rect(0,0,139,87,'yellow')
    for i,h in enumerate([17,29,44,26,55,37,19,43,25]):
        c += rect(15+i*13,(87-h)/2,5,h,'#353b2f')
    c += '</g>' + star(35,57,23) + star(354,170,16,'blue')
    c += line(0,327,385,327,'ink',2) + '</g>'
    c += line(58,481,1142,481)
    c += circle(65,508,4,'green') + text(81,513,'ALWAYS MAKING SOMETHING.',13,'muted','mono')
    c += text(1139,513,'OPEN SOURCE, OPEN POSSIBILITIES.  ↗',13,'muted','mono','text-anchor="end"')
    svg('hero',1200,560,c,'ROYIANS / Joshua — Small ideas. Real things.')


def card(name, number, label, title, subtitle, kind):
    c = text(28,37,number+' / '+label,13,'muted','mono', 'letter-spacing="1"')
    c += text(548,39,'↗',24,'muted',extra='text-anchor="end"')
    c += line(28,56,552,56)
    c += text(26,117,title,48,'ink','serif','letter-spacing="-2"')
    c += text(29,148,subtitle,13,'muted','mono')
    if kind == 'cue':
        c += circle(440,193,70,'orange')
        c += rect(266,168,131,86,'ink', 'rx="5"')
        c += rect(274,176,115,70,'paper', 'rx="2"')
        c += f'<path d="M318 191L349 211L318 231Z" fill="{P["orange"]}"/>'
        c += rect(404,182,124,83,'paper', f'stroke="{P["ink"]}" stroke-width="2" rx="4"')
        for i,h in enumerate([17,29,43,23,52,29,38,17]):
            c += rect(419+i*13,223-h/2,4,h,'orange')
        c += star(248,224,15,'blue')
    elif kind == 'print':
        c += '<g transform="translate(287 161) rotate(-12)">'
        c += rect(0,0,131,113,'blue') + rect(15,14,101,5,'paper')
        c += rect(15,34,55,52,'paper') + '</g>'
        c += '<g transform="translate(398 137) rotate(9)">'
        c += rect(0,0,119,132,'paper',f'stroke="{P["ink"]}" stroke-width="2"')
        c += text(14,51,'Aa',41,'ink','serif') + rect(15,67,87,3,'orange')
        for y in [83,95,107]: c += line(15,y,102,y,'line',2)
        c += '</g>'
        c += star(253,213,18,'blue')
    elif kind == 'room':
        c += f'<path d="M335 164L424 123L532 175V247L442 289L335 235Z" fill="{P["green"]}" opacity=".18"/>'
        c += f'<path d="M335 235L424 193L532 247L442 289Z" fill="{P["green"]}" opacity=".4"/>'
        c += line(424,123,424,193,'green',2)
        c += rect(356,172,37,42,'paper',f'stroke="{P["green"]}" stroke-width="2"')
        c += line(374,172,374,214,'green',2) + line(356,193,393,193,'green',2)
        c += rect(426,218,51,23,'orange') + rect(435,207,51,13,'yellow')
        c += rect(483,186,18,32,'green') + circle(493,178,15,'green')
        c += star(278,221,15,'orange')
    else:
        c += rect(275,175,257,96,'ink', 'rx="7"')
        c += rect(287,187,233,72,'paper','rx="2"')
        for x in range(298,519,22): c += line(x,197,x,247,'line',1)
        for y in range(197,248,10): c += line(297,y,510,y,'line',1)
        for x,y,w in [(298,227,35),(333,207,25),(358,217,28),(386,197,32),(417,217,24),(441,207,33),(474,227,35)]:
            c += rect(x,y,w,8,'blue')
        c += star(461,135,23,'blue') + star(251,224,13,'orange')
    c += text(29,271,{'cue':'STORY → SOUND','print':'CANVAS → PAPER','room':'OBJECTS → STORIES','sound':'IDEAS → 8-BIT'}[kind],12,'muted','mono')
    svg(name,580,304,c,title+' — '+subtitle)


def footer():
    c = text(35,61,'R /',30,extra='font-weight="700"')
    c += text(108,61,'Made with curiosity. Shared with you.',28,'ink','serif')
    c += star(1117,51,18) + text(1140,91,'ROYIANS',12,'muted','mono','text-anchor="end" letter-spacing="3"')
    svg('footer',1200,112,c,'Made with curiosity. Shared with you.')


for theme, P in PALETTES.items():
    hero()
    card('cuepoint','01','CREATIVE TOOLS','Cuepoint','A LOCAL-FIRST AI STUDIO','cue')
    card('foliq','02','DESIGN ENGINEERING','Foliq','THOUGHTFULLY PUT TO PAPER','print')
    card('dicha','03','EVERYDAY LIFE','Dicha','A LITTLE ROOM FOR YOUR LIFE','room')
    card('famistudio','04','MUSIC EXPERIMENTS','FamiStudio','SMALL CHIPS. BIG FEELINGS.','sound')
    footer()

print(f'Generated 12 SVG assets in {OUT}')
