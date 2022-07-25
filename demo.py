# function in python
def func():
    return 0

x = 0

def func1():
    x = 2
    print("FUNC1: VALUE OF X AT END OF FUNC1 : %d"%x)


def func2():
    global x
    x = 3
    print("FUNC2: VALUE OF X AT END OF FUNC2 : %d"%x)

print("VALUE OF X BEFORE FUNC1: %d"%x)
func1()
print("VALUE OF X AFTER FUNC1: %d"%x)
func2()
print("VALUE OF X AFTER FUNC2: %d"%x)


x = "AAA"

print("VALUE OF X %s %d"%(x,5))

x = func1
x()

x = func2
print("VALUE OF X BEFORE FUNC2"+str(x))
x()
print("VALUE OF X AFTER FUNC2: %d"%x)

arr = []
arr.append(4)
arr = [42,3]
print(arr)


import numpy as np

arr = np.arange(1,100,2)
print(arr)