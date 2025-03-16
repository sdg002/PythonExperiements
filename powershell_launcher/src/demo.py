import sys

print(f"Hello world, found {len(sys.argv)} command line arguments")
print(f"sys.executable={sys.executable}")
print(f"sys.path={sys.path}")

for index,arg in enumerate(sys.argv):
    print(f"\t{index}.....{arg}")

import numpy as np
print("Some numpy stuff")
np.ones([4,4])