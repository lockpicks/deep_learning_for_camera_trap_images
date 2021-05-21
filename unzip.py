# !/usr/bin/env python3
# https://askubuntu.com/questions/86849/how-to-unzip-a-zip-file-from-the-terminal
import sys
from zipfile import PyZipFile
for zip_file in sys.argv[1:]:
    print("unzipping", zip_file)
    pzf = PyZipFile(zip_file)
    pzf.extractall()