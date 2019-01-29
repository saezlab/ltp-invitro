# Data and workflow for feature filtering and identification in the `in vitro` lipid transfer protein ligand screen

We have 3 layers of code here:

* `lipyd` is our generic lipidomics module, available in `lipyd` repo, branch `dev4`
* `ltp` is a module with the LTP specific code, available in `ltp_ms` repo, branch `ltp`
* then in the `ltp_invitro` repo there are most of the input files for the in vitro screen, except mgf files and the old SwissLipids & LipidMaps database files because those are huge; and this repo includes a small script called `workflow` with just 3 lines of code for running the analysis

This is all what you need to run the process.
Of course it runs by default with our current settings.
Some settings can be modified by passing arguments to the
`ltp.featureproc.Screen` class. Apart from these options,
new or custom modifications on the analysis method can be
done by modifying the code in the `ltp.featureproc.Screen`
class. This class is not well documented but very clearly
structured code.
