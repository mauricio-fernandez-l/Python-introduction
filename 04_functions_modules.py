# %% Basic

def f(x):
    internal_variable = 5
    computation = x + internal_variable
    return computation

print(f(10))

# %% Optional key arguments

def f2(x, y, op1="something", op2=10):
    print("\nBegin routine")
    v = x + y
    if len(op1) > 10:
        print(op1)
    if op2 > 10:
        v += op2
    return v

# print(f2(1))
print(f2(1, 2))
print(f2(1, 2, op2=5))
print(f2(1, 2, op2=15))
print(f2(1, 2, op2=5, op1="This is a longer sentence"))

# %% Develop your own module with functions

import sys
sys.path.append('.') # required for autocompletion in Spyder IDE

import package.module as pm

folder = '.'
pm.list_content(folder) # Use Ctrl+D to go to definition

