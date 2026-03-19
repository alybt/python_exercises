import multiprocessing
import os

# Solution 1
cpu_count = multiprocessing.cpu_count()

print(cpu_count)

# Solution 2
cpu_count = os.cpu_count()
print(cpu_count)



