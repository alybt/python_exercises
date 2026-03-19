import os
import psutil
from subprocess import call

call("dir", shell = True)
os.system("dir")
print(psutil.cpu_count())
