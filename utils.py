"""
utils.py

useful functions

"""

from os import PathLike
import shutil
from pathlib import Path
import sys
import requests
import gzip
import tarfile


def bag_wget(uri: str, output_file: PathLike | str, overwrite=True) -> None:
    """
    bag_wget Pure python simplified wget

    Args:
        uri (str): The source for the file to download
        output_file (PathLike): The location to write the file.
        overwrite (bool): If False, do not attempt to overwrite the file.
    """
    out_path = Path(output_file)
    if not overwrite and out_path.exists():
        print(f"File {output_file} already exists.")
        return
    try:
        r = requests.get(uri)
        with open(out_path, "wb") as f:
            for chunk in r.iter_content(chunk_size=16 * 1024):
                f.write(chunk)
    except Exception as e:
        print(f"Unable to download file from '{uri}'", file=sys.stderr)
        print(f"Raised exception: {e}")


def bag_gzip(file_name: PathLike | str) -> None:
    """
    gzip Pure python simplified gzip

    Args:
        file_name (PathLike): the file to gzip
    """
    file_path = Path(file_name)
    if not file_path.exists():
        print(f"Unable to locate '{file_name}.'", file=sys.stderr)
        return
    try:
        with open(file_path, "rb") as f_in:
            with gzip.open(file_path.as_posix() + ".gz", "wb") as f_out:
                shutil.copyfileobj(f_in, f_out)
    except Exception as e:
        print(f"Unable to compress {file_name}.", file=sys.stderr)
        print(f"Raised execptiopn {e}")


def bag_extract(
    file_name: PathLike | str, output_dir: PathLike | str | None = None
) -> None:
    file_path = Path(file_name)
    if not file_path.exists():
        print(f"Unable to locate: '{file_name}'.", file=sys.stderr)
        return

    if output_dir:
        output_path = Path(output_dir)
    else:
        output_path = file_path.cwd()
    if not output_path.exists() or not output_path.is_dir():
        print(f"'{output_dir}' is not a valid directory.", file=sys.stderr)
        return

    try:
        tar = tarfile.open(file_path, mode="r:gz")
        tar.extractall(filter="tar", path=output_path)
    except Exception as e:
        print(f"Unable to extract contents of {file_name}.", file=sys.stderr)
        print(f"Raised exception {e}")
    finally:
        tar.close()
