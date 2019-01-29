# Data and workflow for feature filtering and identification in the *in vitro* lipid transfer protein ligand screen

We have 3 layers of code here:

* `lipyd` is our generic lipidomics module, available in https://git.embl.de/grp-gavin/lipyd repo, branch `dev4`
* `ltp` is a module with the LTP specific code, available in https://git.embl.de/grp-gavin/ltp_ms repo, branch `ltp`
* then in this repo you find most of the input files for the in vitro screen, except MGF files and the old SwissLipids & LipidMaps database files because those are huge; and this repo includes a small script called `workflow_features.py` with just 3 lines of code for running the analysis

This is all what you need to run the process.
Of course it runs by default with our current settings.
Some settings can be modified by passing arguments to the
`ltp.featureproc.Screen` class. Apart from these options,
new or custom modifications on the analysis method can be
done by modifying the code in the `ltp.featureproc.Screen`
class. This class is not well documented but very clearly
structured code.

To run the analysi follow the steps below:

```
# Clone this repo:
git clone git@git.embl.de:grp-gavin/ltp_invitro.git

# Enter the directory:
cd ltp_invitro

# Clone the repo of the `lipyd` module:
git clone --single-branch --branch dev4 git@git.embl.de:grp-gavin/lipyd.git

# Link the directory of the `lipyd` module to your working directory:
ln -s lipyd/src/lipyd ./

# Clone the repo of the `ltp` module:
git clone --single-branch --branch ltp git@git.embl.de:grp-gavin/ltp_ms.git

# Link the directory of the `ltp` module to your working directory:
ln -s ltp_ms/src/ltp ./

# Link your directory with all MGF files below the `data` directory:
ln -s /where/you/store/mgf/files ./data/mgf

# Modify the paths near the top of `ltp/featureproc.py` to point to the
# instances of SwissLipids and LipidMaps databases you desire to use.
# If you want to use the most recent versions comment out those lines.

# Open a Python3 shell and run the analysis
# as you see in `workflow_features.py`:

>>> from ltp import featureproc
>>> s = featureproc.Screen(screen = 'invitro')
>>> s.main()
```

It's that easy! :)
