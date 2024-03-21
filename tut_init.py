from tqdm import tqdm
import requests
from pathlib import Path
import sys
import tarfile

def download_pbmc_matrices(url: str, fname: str) -> None:

    r = requests.get(url, stream=True)
    with open(fname, 'wb') as f:
        content_len = r.headers.get('content-length')
        assert content_len is not None
        # total_length = int(content_len)
        for chunk in tqdm(r.iter_content(chunk_size=1024)): 
            if chunk:
                f.write(chunk)
                f.flush()

def install_pbmc_matrices(folder: str="data") -> None:

    url = "http://cf.10xgenomics.com/samples/cell-exp/1.1.0/pbmc3k/pbmc3k_filtered_gene_bc_matrices.tar.gz" 
    fname = "pbmc3k_filtered_gene_bc_matrices.tar.gz"
    data_path = Path(folder)
    file_path = data_path / fname

    if file_path.exists():
        print("pbmc file already downloaded")

    if not data_path.exists():
        data_path.mkdir()

    download_pbmc_matrices(url, fname)
    if not file_path.exists():
        print("Error reading matrix file!", file=sys.stderr)

    t = tarfile.open(file_path)
    t.extractall(filter=tarfile.tar_filter, path="data")
    t.close()

    output_path = data_path / Path("filtered_gene_bc_matrices/hg19")
    assert output_path.exists()
    assert output_path.is_dir()
