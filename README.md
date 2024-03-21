# Baglole Lab Tutorial

This directory contains the files for tutorials held on April 3 and 10, 2024 in the Baglole Lab.

**Author**: David Eidelman

**Advisor**: Nicole Heimbach

**Last Updated**: March 21, 2024

## Clone the files we will use for the tutorial

Open the terminal and move to whereever you want this project to be stored.  Then execute the following at the command line:

```bash
git clone "https://github.com/deidelma/baglabtut"
```
This will create a directory called `baglabtut`.  Use `cd` to enter the directory:

```bash
cd baglabtut
```

## Single Cell Data

This tutorial is partially based on the [Scanpy cluster analysis tutorial](https://scanpy-tutorials.readthedocs.io/en/latest/pbmc3k.html).

To access the necessary data, please use the following commands in the terminal:

```bash
# mkdir data (only if data does not already exist)
wget http://cf.10xgenomics.com/samples/cell-exp/1.1.0/pbmc3k/pbmc3k_filtered_gene_bc_matrices.tar.gz -O data/pbmc3k_filtered_gene_bc_matrices.tar.gz
cd data; tar -xzf pbmc3k_filtered_gene_bc_matrices.tar.g
cd - # get back to where you started from
```
This depends on the `wget` command being installed on your computer. `wget` is present in Linux and MacOS X by default. If for some reason it is not yet installed (e.g., you're on Windows), simply use conda (or mamba) to install it as follows:

```bash
conda activate baglabtut # if not already activated
conda install -c conda-forge wget # it is important to specify the conda-forge channel
```


