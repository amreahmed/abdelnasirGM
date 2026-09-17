"""Download local Arabic and display fonts for the native HTML version."""
import re
from pathlib import Path
from urllib.request import Request, urlopen

root = Path(__file__).resolve().parents[1]
for family,slug in [('Cairo:wght@400;600;700;800;900','cairo'),('Oswald:wght@600;700','oswald')]:
    url='https://fonts.googleapis.com/css2?family='+family+'&display=swap'
    request=Request(url,headers={'User-Agent':'Mozilla/5.0'})
    css=urlopen(request,timeout=30).read().decode()
    for index,remote in enumerate(dict.fromkeys(re.findall(r'url\((https:[^)]+)\)',css))):
        extension=remote.rsplit('.',1)[-1]
        name=f'{slug}-{index}.{extension}'
        (root/'assets'/name).write_bytes(urlopen(remote,timeout=30).read())
        css=css.replace(remote,name)
    (root/'assets'/f'{slug}.css').write_text(css,encoding='utf-8')
print('Arabic and display fonts downloaded locally.')
