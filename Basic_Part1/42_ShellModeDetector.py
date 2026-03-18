import struct
import platform

print(struct.calcsize("P") * 8)

architecture = platform.architecture()[0]
print(architecture)

print(struct.calcsize("P") * 8)