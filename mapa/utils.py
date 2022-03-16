import tempfile
from functools import wraps
from pathlib import Path
from time import time

import click


def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        # start_msg = f"{f.__name__} ..."
        # click.echo(f"{start_msg:<40s}", nl=False)
        result = f(*args, **kw)
        te = time()
        end_msg = f"✅ ({round(te - ts, 1)}s)"
        click.echo(f"{end_msg:<20s}")
        return result

    return wrap


def TMPDIR() -> Path:
    tmpdir = Path(tempfile.gettempdir()) / "map2stl"
    if not tmpdir.is_dir():
        tmpdir.mkdir()
    return tmpdir


def _path_to_merged_tiff(bbox_hash: str) -> Path:
    return TMPDIR() / f"merged_{bbox_hash}.tiff"


def _path_to_clipped_tiff(bbox_hash: str) -> Path:
    return TMPDIR() / f"clipped_{bbox_hash}.tiff"
