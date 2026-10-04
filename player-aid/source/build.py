"""Build the player-aid PDF from template.html + style.css (+ wf/f.css fonts, icons/).

template.html previews directly in a browser. This script inlines the fonts and
icons as data URIs so the HTML is self-contained, then renders it with Chromium.
"""
import base64, re, urllib.request, pathlib

def read(p): return pathlib.Path(p).read_text()

def embed_font(m):
    data = urllib.request.urlopen(m.group(1)).read()
    return "url(data:font/ttf;base64," + base64.b64encode(data).decode() + ")"

def embed_icon(m):
    data = pathlib.Path(m.group(1)).read_bytes()
    return 'src="data:image/jpeg;base64,' + base64.b64encode(data).decode() + '"'

fonts = re.sub(r"url\((https://[^)]*)\)", embed_font, read('wf/f.css'))
html = read('template.html')
html = html.replace('<link rel="stylesheet" href="wf/f.css">', f'<style>{fonts}</style>')
html = html.replace('<link rel="stylesheet" href="style.css">', f'<style>{read("style.css")}</style>')
html = re.sub(r'src="(icons/[^"]+\.jpg)"', embed_icon, html)
open('aid.html', 'w').write(html)

from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(); pg.set_content(html); pg.wait_for_timeout(500)
    h = pg.evaluate("()=>{const p=document.querySelector('.page');return [p.scrollHeight,p.clientHeight]}")
    print('scroll/client', h)
    pg.pdf(path='../captain-sonar-player-aid.pdf', format='Letter', print_background=True, margin={'top': '0', 'bottom': '0', 'left': '0', 'right': '0'})
    b.close()

import pymupdf
d = pymupdf.open('../captain-sonar-player-aid.pdf'); print('pages', len(d))
d[0].get_pixmap(dpi=110).save('render.png')
bl = [b for b in d[0].get_text('blocks') if b[4].strip()]
print(sorted(b[3] for b in bl)[-4:])
