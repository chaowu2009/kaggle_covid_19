import os
import sys
import glob

all_files = glob.glob("*.py")
for file in all_files:
    print(file)
    cmd = "autopep8 --max-line-length=160 --in-place --aggressive --aggressive " + file
    os.system(cmd)

all_files = glob.glob("src/*.py")
for file in all_files:
    print(file)
    cmd = "autopep8 --max-line-length=160 --in-place --aggressive --aggressive " + file
    os.system(cmd)
