import tempfile
from pathlib import Path
import tut_init


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
        
        

        
