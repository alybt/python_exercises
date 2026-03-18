import platform
import os
import sys
import sysconfig


# Solution 1
print("Name of the operating system: ", os.name)
print("\nName of the OS system: ", platform.system())

print("\nVersion of the operating system: ", platform.release())

# Solution 2
print("os.name                      ", os.name)
print("sys.platform                 ", sys.platform)
print("platform.system()            ", sysconfig.get_platform())
print("platform.machine()           ", platform.machine())
print("platform.architecture()      ", platform.architecture())
