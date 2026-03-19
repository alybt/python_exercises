import os 

# Solution 1
print('*----------------------------------*')
print(os.environ)
print('*----------------------------------*')
print(os.environ['USERPROFILE'])
print('*----------------------------------*')
print(os.environ['PATH'])
print('*----------------------------------*')

print('\n')
# Solution 2
for data in os.environ:
    print(data)
    print('-' * 15)
    print(os.environ[data])
    print('=' * 30 )


print('\n')
# Solution 3

for item, value in os.environ.items():
    print('{}: {}'.format(item, value))
