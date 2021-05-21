# !/usr/bin/env python3
# https://askubuntu.com/questions/86849/how-to-unzip-a-zip-file-from-the-terminal

# if you are unzipping the phase folders, prior to unzipping,
# rename the zip files to phaseX_base or etc.
# so it does not conflict with the existing folders named phase1, phase2, etc.

import sys
from zipfile import PyZipFile
for zip_file in sys.argv[1:]:
    print("unzipping", zip_file)
    pzf = PyZipFile(zip_file)
    pzf.extractall()