"""Download the public video assets used in the original portfolio."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1] / 'assets'
VIDEOS = ['b581e92398f6404deadb5962b4291769', 'fc277580235d6c7b91a9d26ef7196d6f', '5bbefa45369ebd9e81607568fe21ad18', '5bd6196d2e6c27e50aca11290510b85a', 'dec48298309ba7e6f316a016afdac9a6', '8db2111d3cf27b80e9ea14bc44a2721b', '51239c88e6b0873382bacd666be2c082', 'fadf2fb2ae62dc52e622ee798e41a83a', 'e1bfb0e9a7cdb810e47b45bf47d8ba3d', '7065f05a105f58048d3ab635a8408094', 'e98eaed63c51bbf003b9656489a3e1d5', 'b6ccfc6f715b86fc948e175fccf24779', 'f90b7368f09ec91fc342589f2357b04f', '7a4c701af3af7fdab97ae30b9129e2b3', '2b34d574c9a07b1037feba5d2127dde1', 'fb0dbd6a8b00ce53519709dd77068bd3']

def download(name):
    target = ROOT / (name + '.mp4')
    if target.exists():
        return f'Exists: {target.name}'
    url = 'https://abdelnassergmportfolio.my.canva.site/_assets/video/' + target.name
    try:
        with urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=90) as response:
            data = response.read()
        if b'ftyp' not in data[:40]:
            return f'FAILED: {name}: not an MP4'
        target.write_bytes(data)
        return f'Saved: {target.name} ({len(data):,} bytes)'
    except Exception as error:
        return f'FAILED: {name}: {error}'

if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=4) as pool:
        for result in pool.map(download, VIDEOS):
            print(result, flush=True)
