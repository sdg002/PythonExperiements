import sys
import os
import time

#
#Demonstrates how to get created time and modified time of a folder
#
#
folder=sys.argv[1]
files = os.scandir(path=folder)
print(f"Going to search in {folder=}")
for file in files:
    ct_secs=os.path.getctime(file.path)
    ct_display = time.ctime(ct_secs)
    mt_secs=os.path.getmtime(file.path)
    print(f"{file}, ctime={ct_secs} secs, ctime={ct_display} mtime={time.ctime(mt_secs)}")
