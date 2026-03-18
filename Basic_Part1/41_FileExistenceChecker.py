import os.path

# Solution 1
print(os.path.isfile('main.txt'))
print(os.path.isfile('main.py'))

# Solution 2
print(os.path.exists('main.txt'))
print(os.path.exists('main.py'))

# Solution 3
print(os.getcwd())

try: 
    my_file = open('main.py')
    my_file.close()
    print("File found!")
except FileNotFoundError:
    print("File not found!")



