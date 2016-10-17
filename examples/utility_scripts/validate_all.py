
# Utility to validate all created NWB files

# This validates the files using format specifications that are
# stored external to the NWB file.

# NWB files that include a copy of the format specifications used to make
# the file within the file, can also be validated by just specifying the
# file name as an argument to nwb_validate.py
# (This is demonstrated by the "internal_validate.sh" script).


import sys
import glob
import os, fnmatch
from subprocess import check_output

# global constants
txt_output_dir="../text_output_files/validate"
nwb_dir="../created_nwb_files"
create_scripts_dir="../create_scripts"
extensions_dir="../create_scripts/extensions"

# extensions needed for validating some NWB files:
# format is script stem: extension (names separated by commas if more than one)
needed_extensions = {
    'analysis-e': 'e-analysis.py',
    'behavior-e': 'e-behavior.py',
    'closed_interface-e': 'e-closed_interface.py',
    'general-e': 'e-general.py',
    'interface-e': 'e-timeseries.py,e-interface.py',
    'module-e': 'e-module.py,e-interface.py,e-timeseries.py',
    'interval-e': 'e-interval.py',
    'intracellular-e': 'e-intracellular.py',
    'timeseries-e': 'e-timeseries.py',
    'trajectorySeries-e': 'e-trajectorySeries.py',
    'trajectorySeries2-e': 'e-trajectorySeries2.py',
}


def save_output(stem, output):
    global output_option, txt_output_dir
    if output_option in ('f', 'b'):
        outpath = os.path.join(txt_output_dir, stem + ".txt")
        with open(outpath, "w") as f:
            f.write(output)
    if output_option in ('s', 'b'):
        print output
        
        
def validate_nwb_file(stem, file):
    global needed_extensions, extensions_dir
    command = ['python', '-m', 'nwb.nwb_validate', file]
    if stem in needed_extensions:
        extensions = needed_extensions[stem]
        # add directory for extensions in front of each extension
        extensions = ",".join([os.path.join(extensions_dir, x) for x in extensions.split(',')])
        command.append(extensions)
    command_str = " ".join(command)
    print "doing", command_str
    output = "command was: " + command_str + "\n"
    output += check_output(command)
    return output
        
def validate_script_files(stem):
    # stem is stem of create script.  Should match either an nwb file or directory containing
    # nwb files
    global needed_extensions, nwb_dir
    path = os.path.join(nwb_dir, stem)
    if os.path.isdir(path):
        # path is directory, validate nwb files in it
        nwb_files = glob.glob(os.path.join(path, "*.nwb"))
        if nwb_files:
            output = []
            for file in nwb_files:
                output.append(validate_nwb_file(stem, file))
            output = "\n".join(output)
            save_output(stem, output)
        else:
            print "No nwb files found in %s" % path
    elif os.path.isfile(path+".nwb"):
        output = validate_nwb_file(stem, path + ".nwb")
        save_output(stem, output)
    else:
        print "nwb file and directory not found for '%s'" % stem
    

def validate_files(output_option):
    global create_scripts_dir
    scripts = glob.glob(create_scripts_dir + "/*.py")
    for script in scripts:
        scriptname = os.path.basename(script)
        stem = scriptname[0:-3]
        validate_script_files(stem)

def display_doc():
    print "format is:"
    print "python %s <output_output>" % sys.argv[0]
    print "output option is:"
    print " 'f' - send output to file"
    print " 's' - send output to screen"
    print " 'b' - send output to both file and screen"

if __name__ == '__main__':
    if len(sys.argv) != 2 or sys.argv[1] not in ('f', 's', 'b'):
        display_doc()
        sys.exit(1)
    output_option = sys.argv[1]
    validate_files(output_option)
    
