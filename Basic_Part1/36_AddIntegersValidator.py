def add_number(a,b):
    if not(isinstance(a, int) and isinstance(b,int)):
        return "Inputs must be integers!"
    return a + b

print(add_number(10,20))
print(add_number(10,20.23))
print(add_number('5',20))
print(add_number('5','6'))
