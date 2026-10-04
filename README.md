# Captain Sonar — Teaching Kit

Materials for teaching **Captain Sonar** (Matagot, 2022) to 8 new players in **Real-Time** mode.

**Assumed setup:** Alpha map · Real-Time (dark) side of every sheet · Hunt mode (4 damage wins) · 4 players per team.

## Contents

```
teaching-script/
  captain-sonar-teaching-script.md   Read-aloud script with stage directions (~25 min + 5 min practice)
player-aid/
  captain-sonar-player-aid.pdf       One-page US Letter reference, one copy per seat
  source/
    build.py                         Builds the PDF from HTML (Playwright + Chromium)
    extract_icons.py                 Re-crops icons from the rulebook PDF
    icons/                           Role and system icons cropped from the rulebook
    wf/f.css                         Google Fonts stylesheet (Exo 2, Share Tech Mono)
```

## Using it

1. Print `player-aid/captain-sonar-player-aid.pdf` once per player.
2. Read the teaching script aloud. Lines in *[italic brackets]* are stage directions.
3. Before play, settle the two rulings the rulebook leaves open (see the script's teacher notes): can a Mine be dropped diagonally, and can a torpedo path pass islands?

## Rebuilding the player aid

```bash
pip install playwright pymupdf pillow
playwright install chromium
cd player-aid/source
python build.py          # writes ../captain-sonar-player-aid.pdf
```

`build.py` downloads the fonts from Google Fonts at build time and embeds them. To re-crop the icons, run `python extract_icons.py <rulebook.pdf>` first.

## Accuracy

Both documents were checked line by line against the official rulebook (`Captain-Sonar-Rules-v5.pdf`). Points the rulebook doesn't state outright: broken systems can still be charged (implied, not explicit); diagonal Mine drops and torpedo paths through islands are unaddressed.

## Copyright

Captain Sonar, its rules, and its iconography are © 2022 Matagot. The icons in `player-aid/source/icons/` are cropped from the rulebook. This is an unofficial fan aid; the rulebook itself is not included. Keep this repo **private** unless you have the publisher's permission to share the icons.
