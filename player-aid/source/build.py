import base64,re,urllib.request,pathlib
css=open('wf/f.css').read()
def emb(m):
    u=m.group(1); data=urllib.request.urlopen(u).read()
    return "url(data:font/ttf;base64,"+base64.b64encode(data).decode()+")"
css=re.sub(r"url\((https://[^)]*)\)",emb,css)
def ic(n): return "data:image/jpeg;base64,"+base64.b64encode(open(f'icons/{n}.jpg','rb').read()).decode()
I={k:ic(k) for k in ['captain','firstmate','engineer','radio','torpedo','mine','drone','sonar','silence','sym_red','sym_green','sym_yellow']}

html=f"""<!doctype html><html><head><meta charset="utf-8"><style>{css}
@page{{size:Letter;margin:0}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:'Exo 2',sans-serif;font-size:7.45pt;line-height:1.25;color:#0d1b2e;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
.page{{width:8.5in;height:11in;padding:.28in .34in .24in;display:flex;flex-direction:column;gap:5pt;overflow:hidden}}
.hdr{{background:#0a2647;color:#fff;border-radius:6pt;padding:7pt 11pt;display:flex;align-items:center;justify-content:space-between;border-bottom:3pt solid #1fa3e0}}
.hdr h1{{font-weight:800;font-style:italic;font-size:21pt;letter-spacing:1.5pt;line-height:1}}
.hdr h1 span{{color:#1fa3e0}}
.hdr .sub{{font-family:'Share Tech Mono';font-size:8pt;letter-spacing:.6pt;color:#bfe6fb;text-align:right;line-height:1.4}}
.hdr .win{{font-weight:800;font-size:10pt;color:#fff;letter-spacing:.4pt}}
.loop{{border:1.2pt solid #1fa3e0;border-radius:6pt;padding:5pt 8pt;background:#eef8fe}}
.lt{{font-weight:800;font-style:italic;font-size:9pt;color:#0a2647;letter-spacing:.5pt;margin-bottom:3pt}}
.steps{{display:grid;grid-template-columns:repeat(4,1fr);gap:5pt}}
.step{{background:#fff;border-radius:4pt;padding:3pt 5pt;border-left:3pt solid #1fa3e0}}
.step b{{display:block;font-size:8pt}}
.mono{{font-family:'Share Tech Mono';}}
.note{{margin-top:3pt;font-weight:600}}
.roles{{display:grid;grid-template-columns:1fr 1fr;gap:6pt}}
.card{{border:1pt solid #9fb7cc;border-radius:6pt;overflow:hidden}}
.ch{{display:flex;align-items:center;gap:6pt;background:#0a2647;color:#fff;padding:3pt 7pt}}
.ch img{{width:22pt;height:22pt;border-radius:50%;object-fit:cover}}
.ch h2{{font-weight:800;font-style:italic;font-size:10.5pt;letter-spacing:.6pt}}
.ch .tag{{margin-left:auto;font-family:'Share Tech Mono';font-size:7pt;color:#bfe6fb}}
ul{{list-style:none;padding:3pt 7pt 4pt}}
li{{padding-left:8pt;position:relative;margin-bottom:1.2pt}}
li:before{{content:'';position:absolute;left:0;top:3.4pt;width:3.2pt;height:3.2pt;background:#1fa3e0;transform:rotate(45deg)}}
.sec{{font-weight:800;font-style:italic;font-size:10pt;color:#0a2647;letter-spacing:.6pt;border-bottom:1.5pt solid #1fa3e0;padding-bottom:1pt;margin-bottom:3pt}}
table{{width:100%;border-collapse:collapse}}
td,th{{padding:2pt 4pt;vertical-align:middle;text-align:left;border-bottom:.6pt solid #c9d8e6}}
th{{font-size:6.8pt;text-transform:uppercase;letter-spacing:.6pt;color:#4a6480;font-weight:600}}
td.icn{{width:24pt}} td.icn img{{width:20pt;height:20pt;border-radius:50%;object-fit:cover;display:block}}
td.nm{{font-weight:800;font-size:8.4pt;white-space:nowrap}}
.pill{{display:inline-block;font-size:6.6pt;font-weight:600;padding:.5pt 4pt;border-radius:6pt;color:#fff;white-space:nowrap}}
.r{{background:#c62828}}.g{{background:#2e8b3a}}.y{{background:#b8860b}}
.bottom{{display:grid;grid-template-columns:1fr 1fr 1fr;gap:7pt}}
.box{{border:1pt solid #9fb7cc;border-radius:6pt;padding:5pt 7pt}}
.box ul,.box ol{{padding:0}}
ol{{padding-left:11pt !important}} ol li{{padding-left:1pt}} ol li:before{{display:none}}
.dmg td{{padding:2pt 3pt}} .dmg td.n{{font-weight:800;font-size:10pt;text-align:center;color:#c62828;width:18pt}}
.syms{{display:flex;gap:7pt;align-items:center;margin:2pt 0 3pt}}
.syms span{{display:flex;align-items:center;gap:3pt;font-weight:600}}
.syms img{{width:15pt;height:15pt;border-radius:50%;object-fit:cover}}
.ftr{{font-family:'Share Tech Mono';font-size:6.4pt;color:#6b8199;display:flex;justify-content:space-between;margin-top:auto}}
.warn{{background:#fff4f2;border-color:#e3a59d}}
</style></head><body><div class="page">

<div class="hdr"><h1>CAPTAIN <span>SONAR</span></h1>
<div class="sub">PLAYER AID · REAL TIME · 8 PLAYERS<br><span class="win">HUNT: DEAL 4 DAMAGE TO WIN</span></div></div>

<div class="loop"><div class="lt">EVERY MOVE — MOVE, CHARGE, BREAK, LISTEN</div>
<div class="steps">
<div class="step"><b>1 · Captain</b>Shout <span class="mono">"Heading North"</span> (or East, South, West). Draw 1 dot of route.</div>
<div class="step"><b>2 · First Mate</b>Mark 1 empty box on any gauge. Say <span class="mono">"OK"</span>.</div>
<div class="step"><b>3 · Engineer</b>Cross out 1 symbol in the panel matching the direction. Say <span class="mono">"OK"</span>.</div>
<div class="step"><b>4 · Enemy Radio Op</b>Draw 1 step in that direction on the clear sheet.</div>
</div>
<div class="note">The Captain calls the next move only after hearing both OKs. No turns: both subs move as fast as their crews allow.</div></div>

<div class="roles">
<div class="card"><div class="ch"><img src="{I['captain']}"><h2>CAPTAIN</h2><span class="tag">STEER · ATTACK</span></div><ul>
<li>Before play, draw a secret X on any water dot. Both Captains shout <span class="mono">"Dive!"</span> to start.</li>
<li>Move 1 dot North, East, South or West. Never diagonally.</li>
<li>Never leave the map, enter an island, or enter any dot your route already touches.</li>
<li><b>Blackout:</b> if no legal move exists, surface immediately.</li>
<li>You activate Torpedo, Mine and Silence, detonate Mines, and call Surface.</li>
<li>Answer enemy hits and Drones truthfully, at once. Sonar: give 1 true fact, 1 false.</li></ul></div>

<div class="card"><div class="ch"><img src="{I['firstmate']}"><h2>FIRST MATE</h2><span class="tag">CHARGE · SCORE</span></div><ul>
<li>Each move, mark 1 box on any gauge. Charge what the Captain asks for.</li>
<li>When a gauge fills, shout <span class="mono">"Torpedo ready!"</span> (or the system's name).</li>
<li>A full gauge stays full until used. Erase the whole gauge after each use.</li>
<li>You activate Drone and Sonar.</li>
<li>Keep score: cross 1 Damage box (top right) per damage. 4th box = sunk.</li>
<li>Ignore the Scenario gauge on the Alpha map.</li></ul></div>

<div class="card"><div class="ch"><img src="{I['engineer']}"><h2>ENGINEER</h2><span class="tag">BREAK · REPAIR</span></div><ul>
<li>Each move, cross 1 symbol in that direction's panel. Say <span class="mono">"OK"</span>.</li>
<li>1+ crossed symbol of a color breaks both systems of that color. Broken systems still charge but can't be used.</li>
<li>Ordering a broken system fails; cross 1 radiation symbol as a penalty.</li>
<li><b>Repair:</b> when all 4 symbols on one circuit line (top half) are crossed, erase those 4.</li>
<li><b>Damage:</b> a full panel, or every radiation symbol crossed = 1 damage. Shout <span class="mono">"Damage!"</span>, then erase your whole sheet.</li>
<li>Repair beats damage when 1 mark causes both.</li></ul></div>

<div class="card"><div class="ch"><img src="{I['radio']}"><h2>RADIO OPERATOR</h2><span class="tag">LISTEN · TRACK</span></div><ul>
<li>Start with a dot in the center of the clear sheet. Draw every enemy move.</li>
<li>Slide the sheet over the map. Their route can't cross islands or itself. It resets when they surface.</li>
<li>Log every clue: Silence (≤4 dots straight, direction unknown), Torpedo impact (enemy ≤4 dots from it), Surface sector, Drone and Sonar answers.</li>
<li>While your own sub is surfaced, you can't write. Memorize enemy moves.</li>
<li>Lost the trail? Erase and restart from the latest clues.</li>
<li>Tell the Captain your best guess, constantly.</li></ul></div>
</div>

<div><div class="sec">SYSTEMS</div>
<div class="syms">Engineer colors: <span><img src="{I['sym_red']}">Red = Mine + Torpedo</span><span><img src="{I['sym_green']}">Green = Drone + Sonar</span><span><img src="{I['sym_yellow']}">Yellow = Silence (+ Scenario)</span></div>
<table><tr><th></th><th>System</th><th>Who</th><th>Effect</th></tr>
<tr><td class="icn"><img src="{I['torpedo']}"></td><td class="nm">Torpedo</td><td><span class="pill r">Captain</span></td><td>Pick a dot up to 4 orthogonal steps from you. Announce <span class="mono">"Torpedo, impact C6!"</span> It explodes there.</td></tr>
<tr><td class="icn"><img src="{I['mine']}"></td><td class="nm">Mine</td><td><span class="pill r">Captain</span></td><td><b>Drop:</b> draw M on a dot next to you, not on your route. Say <span class="mono">"Mine dropped!"</span> <b>Detonate later, any time:</b> <span class="mono">"Stop! Mine at G7!"</span> Detonating needs no gauge and isn't an activation. Any red breakdown blocks it. Mines survive surfacing.</td></tr>
<tr><td class="icn"><img src="{I['drone']}"></td><td class="nm">Drone</td><td><span class="pill g">First Mate</span></td><td>Ask about 1 of the 9 sectors: <span class="mono">"Are you in sector 5?"</span> Enemy answers yes or no, truthfully.</td></tr>
<tr><td class="icn"><img src="{I['sonar']}"></td><td class="nm">Sonar</td><td><span class="pill g">First Mate</span></td><td>Enemy names 2 facts of different types (row, column, sector): 1 true, 1 false. Example: at N12 in sector 9, say <span class="mono" style="white-space:nowrap">"Column N, sector 7."</span></td></tr>
<tr><td class="icn"><img src="{I['silence']}"></td><td class="nm">Silence</td><td><span class="pill y">Captain</span></td><td>Move 0–4 dots in a straight line without saying the direction; show the Engineer by thumb behind the screen. Still a move: First Mate marks 1 box, Engineer marks 1 symbol (fakes it on 0). Route rules apply.</td></tr>
</table></div>

<div class="bottom">
<div class="box"><div class="sec">STOP! — ACTIVATE</div><ol>
<li>Gauge full, and the Engineer confirms no breakdown of that color.</li>
<li>Raise a fist, shout <span class="mono">"Stop!"</span> Everyone lifts pens and listens.</li>
<li>Name the system and resolve it. First Mate erases that gauge.</li>
<li>Resume play.</li></ol>
<p style="margin-top:3pt"><b>Move at least once between 2 activations.</b> Mine detonation and Surface don't count as activations.</p></div>

<div class="box warn"><div class="sec">EXPLOSIONS &amp; DAMAGE</div>
<table class="dmg">
<tr><td class="n">2</td><td><b>Direct hit</b> — explosion on the sub's dot.</td></tr>
<tr><td class="n">1</td><td><b>Indirect hit</b> — on 1 of the 8 surrounding dots.</td></tr>
<tr><td class="n">0</td><td><b>Clear</b> — 2+ dots away.</td></tr>
<tr><td class="n">1</td><td><b>Engineer</b> — full panel or all radiation crossed.</td></tr></table>
<ul style="padding:3pt 0 0">
<li>Your own Torpedo or Mine hurts you too.</li>
<li>Torpedo on a Mine destroys it. Torpedo next to a Mine sets it off (Torpedo resolves first).</li>
<li>Announce all damage, even self-inflicted. 4 damage = sunk.</li></ul></div>

<div class="box"><div class="sec">SURFACING</div>
<ul><li>Captain raises a fist: <span class="mono">"Surfacing in sector 6!"</span></li>
<li><b>Clears:</b> all breakdowns; the route (keep current dot and Mines). <b>Keeps:</b> damage, gauges.</li>
<li>Each crew member traces 1 of the 4 sub sections inside the double hull and initials it.</li>
<li>Enemy Engineer checks it; any line over the hull = redo.</li>
<li>Erase it, say <span class="mono">"Ready to dive!"</span>, Captain shouts <span class="mono">"Dive!"</span></li>
<li>While up: no systems; Radio Op can't write. The enemy keeps moving.</li></ul></div>
</div>

<div class="ftr"><span>Alpha map · Real Time (dark) side · Hunt mode</span><span>Unofficial aid from the Matagot rulebook. Icons © 2022 Matagot.</span></div>
</div></body></html>"""
open('aid.html','w').write(html)
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(); pg.set_content(html); pg.wait_for_timeout(500)
    h=pg.evaluate("()=>{const p=document.querySelector('.page');return [p.scrollHeight,p.clientHeight]}")
    print('scroll/client',h)
    pg.pdf(path='../captain-sonar-player-aid.pdf',format='Letter',print_background=True,margin={'top':'0','bottom':'0','left':'0','right':'0'})
    b.close()
import pymupdf
d=pymupdf.open('../captain-sonar-player-aid.pdf'); print('pages',len(d))
d[0].get_pixmap(dpi=110).save('render.png')
bl=[b for b in d[0].get_text('blocks') if b[4].strip()]
print(sorted(b[3] for b in bl)[-4:])
