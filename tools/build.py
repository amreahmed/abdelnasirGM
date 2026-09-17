"""Rebuild the native HTML portfolio."""
from pathlib import Path
import runpy
runpy.run_path(str(Path(__file__).with_name('build_native.py')), run_name='__main__')
