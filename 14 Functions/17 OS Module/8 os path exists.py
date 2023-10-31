#os.path.exists():

import os

if(os.path.exists("C:/Python128/int2.py")):
    os.remove("C:/Python128/int2.py")
else:
    print("File doesnt exist")
