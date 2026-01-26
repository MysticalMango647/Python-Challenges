'''
print file size of existing .txt file
capture enrror if they exist
'''

import os, sys

path = "example.txt"

try:
    #size = os.path.getsize(path)
    #Other way to get size direct call
    size = os.stat(path).st_size
except OSError:
    print("File Error")
    sys.exit()

print(size)