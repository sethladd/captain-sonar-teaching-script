"""Crop the role and system icons from the Captain Sonar rulebook PDF.

Usage: python extract_icons.py path/to/Captain-Sonar-Rules-v5.pdf
Writes icons/*.jpg, which build.py embeds into the player aid.
"""
import sys, pathlib, pymupdf
from PIL import Image

CROPS = {  # name: (page index, [x0, y0, x1, y1] in PDF points)
    'captain': (1, [77, 103, 148, 173]), 'radio': (1, [436, 103, 506, 173]),
    'firstmate': (2, [58, 103, 128, 173]), 'engineer': (2, [416, 88, 486, 158]),
    'sym_red': (2, [447, 527, 502, 582]), 'sym_green': (2, [564, 527, 620, 583]),
    'sym_yellow': (2, [682, 527, 738, 583]),
    'torpedo': (5, [78, 420, 134, 476]), 'mine': (5, [436, 325, 493, 381]),
    'silence': (6, [415, 94, 472, 151]), 'sonar': (6, [57, 287, 113, 343]),
    'drone': (6, [58, 550, 114, 607]),
}

doc = pymupdf.open(sys.argv[1])
out = pathlib.Path(__file__).parent / 'icons'
out.mkdir(exist_ok=True)
for name, (page, rect) in CROPS.items():
    png = out / f'{name}.png'
    doc[page].get_pixmap(clip=pymupdf.Rect(*rect), dpi=400).save(png)
    im = Image.open(png).convert('RGB'); im.thumbnail((240, 240))
    im.save(out / f'{name}.jpg', quality=88); png.unlink()
print('wrote', len(CROPS), 'icons to', out)
