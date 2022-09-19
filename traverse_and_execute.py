# import required module
import os
import sys
from pathlib import Path


def exec_script_against_file(mypath):
    stream = os.popen('bash ./script_to_exec.sh {}'.format(mypath))
    output = stream.read()
    print(output)

def open_file(mypath):
    with open(mypath, 'r') as myfile:
        myfilecontent = myfile.read()
        print(myfilecontent)


if len(sys.argv) != 2:
    print("Usage: python3 {} {}".format(sys.argv[0], "base_dir"))
    exit(1)


directory = sys.argv[1]

for path in Path(directory).rglob('*'):
    #print(path.name)
    print(path)
    if os.path.isfile(path):
        #open_file(path)
        exec_script_against_file(path)
    
