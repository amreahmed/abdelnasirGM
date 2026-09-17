from pathlib import Path
import re
import sys
from urllib.request import Request, urlopen

root = Path(__file__).resolve().parents[1]
html = (root / 'index.html').read_text(encoding='utf-8')
refs = set(re.findall(r'assets/[^"<> ]+', html))
missing = [name for name in refs if not (root / name).is_file()]
assert not missing, missing
assert html.count('<section ') == 7
assert html.count('<video ') == 16
assert html.count('class="post-card"') == 12
assert html.count('class="caption-note"') == 12
assert 'class="artwork"' not in html
assert 'class="portfolio-section"' not in html
for stylesheet in [root/'styles.css',root/'assets/cairo.css',root/'assets/oswald.css']:
    for reference in re.findall(r'url\([\'\"]?([^\)\'\"]+)', stylesheet.read_text(encoding='utf-8')):
        assert (stylesheet.parent/reference).is_file(), reference
for video in (root/'assets').glob('*.mp4'):
    data = video.read_bytes()
    assert b'ftyp' in data[:40], video.name
    offset = 0
    boxes = []
    while offset + 8 <= len(data):
        size = int.from_bytes(data[offset:offset+4], 'big')
        boxes.append(data[offset+4:offset+8])
        if size == 1:
            size = int.from_bytes(data[offset+8:offset+16], 'big')
        if size == 0:
            offset = len(data)
            break
        assert size >= 8 and offset+size <= len(data), f'Truncated MP4: {video.name}'
        offset += size
    assert b'moov' in boxes and b'mdat' in boxes, video.name
    assert offset == len(data), video.name
if '--static' not in sys.argv:
    request = Request('http://127.0.0.1:4173/assets/b581e92398f6404deadb5962b4291769.mp4', headers={'Range':'bytes=0-99'})
    with urlopen(request) as response:
        assert response.status == 206
        assert len(response.read()) == 100
    print('PASS: local preview HTTP range/seek support.')
print(f'PASS: {len(refs)} local references; local fonts/background; 7 native sections; 12 HTML caption cards; 16 complete MP4 containers.')
