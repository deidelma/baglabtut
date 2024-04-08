import tempfile
from pathlib import Path

import anndata
import pandas as pd
import tut_init
from rdsad import create_adata, read_10x_data


def test_download_pbmc_matrices():
    url = "http://cf.10xgenomics.com/samples/cell-exp/1.1.0/pbmc3k/pbmc3k_filtered_gene_bc_matrices.tar.gz"
    fname = "crap.tar.gz"
    with tempfile.TemporaryDirectory() as dir_name:
        dir_path = Path(dir_name)
        file_path = dir_path / fname
        assert not file_path.exists()
        tut_init.download_pbmc_matrices(url, file_path.as_posix())
        assert file_path.exists()


def test_install_pbmc_matrices():
    with tempfile.TemporaryDirectory() as dir_name:
        tut_init.install_pbmc_matrices(folder=dir_name)
        out_path = Path(dir_name) / "filtered_gene_bc_matrices/hg19"
        assert (out_path / Path("barcodes.tsv")).exists()


def test_read_10x_data() -> None:
    mtx, barcodes, features = read_10x_data(Path("data"))
    assert isinstance(features, pd.DataFrame)
    adata = create_adata(mtx, barcodes=barcodes, features=features)
    assert adata is not None
    assert isinstance(adata, anndata.AnnData)
    adata.write_h5ad(Path("data/pbmc.h5ad"))
