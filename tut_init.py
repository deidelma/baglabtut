from os import PathLike
from tqdm import tqdm
import requests
from pathlib import Path
import sys
import tarfile
import shutil
import gzip
from rdsad import seurat


def download_pbmc_matrices(url: str, fname: PathLike| str) -> None:
    if isinstance(fname, str):
        fname = Path(fname)
    r = requests.get(url, stream=True)
    with open(fname, 'wb') as f:
        content_len = r.headers.get('content-length')
        assert content_len is not None
        # total_length = int(content_len)
        for chunk in tqdm(r.iter_content(chunk_size=1024)): 
            if chunk:
                f.write(chunk)
                f.flush()


def to_gzip(file_path: Path) -> None:
    with open(file_path, 'rb') as f_in:
        out_path = Path(file_path.as_posix() + '.gz')
        with gzip.open(out_path, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)    


def gzip_matrix_files(folder: Path ) -> None:
    files = ['barcodes.tsv', 'features.tsv','matrix.mtx']
    for file in files:
        to_gzip(folder / Path(file))


def install_pbmc_matrices(folder: str = "data") -> None:

    url = "http://cf.10xgenomics.com/samples/cell-exp/1.1.0/pbmc3k/pbmc3k_filtered_gene_bc_matrices.tar.gz" 
    fname = "pbmc3k_filtered_gene_bc_matrices.tar.gz"
    data_path = Path(folder)
    file_path = data_path / fname

    if file_path.exists():
        print("pbmc file already downloaded")

    if not data_path.exists():
        data_path.mkdir()

    download_pbmc_matrices(url, file_path)
    if not file_path.exists():
        print("Error reading matrix file!", file=sys.stderr)

    t = tarfile.open(file_path)
    t.extractall(filter=tarfile.tar_filter, path=folder)
    t.close()

    output_path = data_path / Path("filtered_gene_bc_matrices/hg19")
    assert output_path.exists()
    assert output_path.is_dir()

    shutil.move(output_path / "barcodes.tsv", data_path / "barcodes.tsv")
    shutil.move(output_path / "genes.tsv", data_path / "features.tsv")
    shutil.move(output_path / "matrix.mtx", data_path / "matrix.mtx")

    assert (data_path / "barcodes.tsv").exists()

    gzip_matrix_files(data_path)

    