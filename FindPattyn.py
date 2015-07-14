#find files in os 

import os
import sys
import re

pattern = ''.join(sys.argv[1:])

for path,folder,files in os.walk(os.getcwd()):
    for files in files:
        if re.findall(pattern,open(path+"/"+files).read()):
            print files
