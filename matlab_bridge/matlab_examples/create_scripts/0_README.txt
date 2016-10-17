This directory "matlab_bridge/matlab_examples/create_scripts" contains example
matlab scripts to create example NWB files.

To run these scripts first install the matlab bridge as described in
file mablab_bridge/0_INSTALL.txt

Then to run the scripts, cd to this directory in matlab.  Type
the name of each script to run it, or "run_all_scripts" to 
run them all.

Several types of scripts require additional files.  These are:


(1) Scripts that required input data.

Scripts with with name starting with "crcns") require data in the
"../source_data" directory.  This data must be downloaded
and placed inside the ../source_data directory.  Instructions
for doing this are in the examples/0_README.txt file
(i.e. the readme in the directory above this one).


(2) Scripts that require extensions.

Scripts that have name ending with "-e.py" require one or more "extensions"
(files that define extensions to the NWB format).  The extensions are
stored in directory "extensions".  Usually the name of the extension
used with the script will be the same as the name of the create script,
except "e-" will be in front of the extension.

The convention of having "e-" in front of the extension (and "-e" at the
end of the create script name) is only used for these examples.  Any name for the
create script and extension(s) can be used as long as the actual name of the
extension(s) are referenced by the create script and passed as parameters to
nwb_validate.py when validating NWB files created using one or more extensions.
