import functools

# Solution 1
for i in range(0, 10):
    print('*', end = "")

print("\n") 

# Solution 2
printf = functools.partial(print, end="")

for i in range(0,10):
    printf('*')

# Solution 3
print("\n") 
i = 0 
while i < 10:
    print('*', end = '')
    i = i + 1