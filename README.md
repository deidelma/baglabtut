# Baglole Lab Tutorial

This directory contains the files for tutorials held on April 3 and 10, 2024 in the Baglole Lab.

**Author**: David Eidelman

**Advisors**: Nicole Heimbach, Emily Wilson

**Last Updated**: April 1, 2024

## Clone the files we will use for the tutorial

Open the terminal and move to whereever you want this project to be stored.  Then execute the following at the command line:

```bash
git clone "https://github.com/deidelma/baglabtut"
```
This will create a directory called `baglabtut`.  Use `cd` to enter the directory:

```bash
cd baglabtut
```

There is also a zip file on the SharePoint site under "coding tutorial".  After you unzip the file, it will create a
directory with the same information as the one above.  Use `cd` to enter the directory:
```bash
cd baglabtut
```

## Install the tutorial environment

The goal is to give you the skills you need to complete the current [scanpy tutorial](https://scanpy.readthedocs.io/en/stable/tutorials/basics/clustering.html) on processing and clustering single cell RNA data.


To complete the exercises in this tutorial and to be able to complete the processing and clustering tutorial on the scanpy site, you need to install a number of prerequisites.  Here are a set of commands that should work:

```bash
conda create -n baglab -c conda-forge python jupyter scanpy scikit-image pooch igraph openpyxl -y
```
or, if you installed micromamba:

```bash
micromamba create -n baglab -c conda-forge python jupyter scanpy scikit-image pooch igraph openpyxl -y
```
**Note:** the name `baglab` is arbitrary.  You may choose any name you like.

## An easier way

To help make things simpler, you can make use of the file "conda-requirements.txt" as follows:

```bash
conda create --name baglab --file conda-requirements.txt -c conda-forge -y
```

## Legacy workflow

If you want to complete the legacy workflow tutorial from 2017, you will need to instal specific versions of scanpy and other packages.  Unfortunately, these are not available on conda-forge.  The file `baglab.yml` has been created to allow you to create an an environment that works with the legacy code.  To install this, once you are in the directory, use the conda program (or micromamba if you installed that instead) to issue the following command :

*Note:* The command is different than that used above. It is `conda env create` not `conda create`.

```bash
conda env create -f baglab.yml
```
or

```bash
micromamba env create -f baglab.yml
```
The file `baglab.yml` contains the instructions to create an environment that can run the legacy version of the the [scanpy cluster analysis tutorial](https://scanpy-tutorials.readthedocs.io/en/latest/pbmc3k.html).  


## Activate the tutorial environment
Once you have created the environment, which can take a few minutes, you should be ready to activate it. Activation is necessary to provide a complete and consistent set of libraries.

To activate the environment, you need to use the following command using the name you chose for the given environment (e.g. `baglab`):

```bash
conda activate baglab
```
or
```bash
micromamba activate baglab
```

Once the environment is activated, the command line prompt will have the prefix: `(baglab)`.

To deactivate the environment, you can use:
```bash
conda deactivate
```
or
```bash
micromamba deactivate
```
## jupyter

To activate jupyter so that you can use notebooks, you need to call it on the command line:
```bash
jupyter lab
```
This should open your default browser.  Using the file list on the left, you can select files to load into jupyter.
Select `tutorial_setup.ipynb` and follow the instructions.

## Single Cell Data

This tutorial is partially based on the [Scanpy cluster analysis tutorial](https://scanpy-tutorials.readthedocs.io/en/latest/pbmc3k.html).

Once you have loaded the needed packages and downloaded the files, please follow the tutorial on the scanpy website.

## Pandas

The setup page also includes some examples of using Pandas to work with DataFrames.

## What about using a server?

The above approach works well on a laptop or desktop computer.  But what about when you need to log in to a remote server to do your analysis?  This requires using a protocol called `ssh`.  There are a number of ways to access this.  You can use a graphical user interface program like [MobaXterm](https://mobaxterm.mobatek.net/) for Windows or [RemoteDesktopManager](https://devolutions.net/remote-desktop-manager/), which have ssh as one of its many functions.  But it is a good idea to become familiar with how to do this inside a terminal emulator.

For Windows, there are several choices, but the standard is [Windows Terminal](https://apps.microsoft.com/detail/9n0dx20hk701?rtc=1&hl=en-ca&gl=CA).  For Mac, there several options but the usual recommendation is to use [iTerm2](https://iterm2.com/).

### Let's go...

To test this out, you need to have an account on a remote server, such as those in Dr. Ding's lab.  To gain access, please speak to someone in the Jingtao in the Ding lab.  Once you have an account on the server, you also need to get access to the virtual private network (VPN).  This requires you to install Cisco Secure Client on your own machine and get a password from the RI IT department.  They will require Dr. Ding's signature before allowing you access.

Once you have been granted access, you are ready to login.  First, activate Cisco Secure Client on your laptop or desktop.  Enter the credentials as instructed by RI IT. 

Now open a terminal emulator window.  Type the following command:

```bash
ssh -L 8888:localhost:8888 <yourname>@cps.jundinglab.org
```
This runs the progam ssh, which opens up a connection to the server and allows you to access a terminal emulator remotely from the server.  The `-L 8888:localhost:8888` ensures that the server's port number 8888 is matched to your own port 8888.  When you run jupyter lab, this will allow the output to be displayed on your desktop rather than the server.  

Note that 8888 is the default port.  You may wish to use a different one.  If you do, make sure that the port you select for the ssh command is the same as for jupyter.  For example, if you want to run jupyter with port 5000, then use the following ssh command:
```bash
ssh -L 5000:localhost:5000 <yourname>@cps.jundinglab.org
```

On some machines, other ports are chosen and you may need to adjust accordingly.  One way to do this is to choose the port that jupyter uses.

Once you have provided your password and logged in, you will be shown a very simple command prompt for the barebones `sh` shell.  To get access to a fully featured shell, you may need to type `bash`, which will put you inside a bash shell, just like on your own machine.

Assuming everything went according to plan, you are ready to start computing.

First, you need a conda environment.  You can use the base one that comes up when you first run bash.  Or, you can use the tutorial one above as a starting point for your own.

Once your conda environment is set up and activated, you can use the following command to start up a jupyter notebook:
```bash
jupyter lab --no-browser --port=8888
```
This command starts up jupyter but doesn't try to open a browser since you are on a terminal emulator.  It sets the port number to the default value of 8888.  But if you chose a different port in the ssh command, use the same number here.

From here on, things should work just like on your own personal computer.

