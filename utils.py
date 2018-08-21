import os
import glob
import re
import sys

# returns a compiled regex for string search
def getRegex(text, delim):
    text_arr = list(map(lambda x: re.escape(x), text.rstrip().split(delim)))
    pattern = ('|').join(text_arr)
    return re.compile(pattern, re.IGNORECASE)

def readFile(path):
    try:
        return open(path, 'r').read()
    except:
        print('Failed to open file.')
        sys.exit(1)

# returns a dictionary of filenames : text
def readDirFiles(path):
    text_dict = {}
    try:
        dir = os.listdir(path)
        for filename in dir:
            text_dict[os.path.basename(filename)] = open(os.path.join(path, filename), 'r').read()
        return text_dict
    except:
        print('Failed to read files from directory.')
        sys.exit(1)

