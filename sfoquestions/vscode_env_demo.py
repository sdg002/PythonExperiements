#
#To run this demo, add a .env file
# add PYTHONPATH to point to the root of the repo
# you will see the difference in sys.path with and without PYTHONPATH
# Summary
# VS Code will automatically apply the variables in the .env file
#

import os
import sys

paths = sys.path
paths.sort(key= len)

print(*paths, sep="\n")

print(f"{os.environ['HELLO']}")