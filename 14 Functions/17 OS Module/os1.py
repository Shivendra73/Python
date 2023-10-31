
import os

if(os.name=='nt'):
    command="ipconfig"
else:
    command="ifconfig"
os.system(command)
