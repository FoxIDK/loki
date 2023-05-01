# Imports.
import sys
import os
from pathlib import Path
from cryptography.fernet import Fernet

# Hide tracebacks - change to 1 for dev mode.
sys.tracebacklimit = 0

# Discovery.
files = [] # Creates a files array.

def findFiles(path):
    dirs = [] # Creates a directory array.
    print("---> source dir |", path)
    for file in os.listdir(path):
        filePath = path + "/" + file
        if file == ".py" or file == "loki.key" or file == "loki.key.bk":
            continue
        
        if not os.path.isfile(filePath):
            dirs.append(filePath)
            continue
        
        print("--> Found file |", filePath)
        files.append(filePath)

    if dirs == []:
        return # No dirs

    for dirPath in dirs:
        print("-! Found sub-dir  |", dirPath)
        findFiles(dirPath)
    
findFiles(".")