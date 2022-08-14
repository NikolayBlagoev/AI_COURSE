
x = 5
print(str(x) + " AAA")
exit()
str()
float()



# function in python
def func():
    # returns 0
    return 0


# Declare a variable
x = 0

def func1():
    x = 2
    # Print with formatting
    # %d -> integer
    # %s -> string
    # %f -> float
    print("FUNC1: VALUE OF X AT END OF FUNC1 : %d"%x)


def func2():
    # Use the x variable outside the function
    global x
    x = 3
    print("FUNC2: VALUE OF X AT END OF FUNC2 : %d"%x)

print("VALUE OF X BEFORE FUNC1: %d"%x)
func1()
print("VALUE OF X AFTER FUNC1: %d"%x)
# call function
func2()
print("VALUE OF X AFTER FUNC2: %d"%x)

# set x equal to string
x = "AAA"

print("VALUE OF X %s %d"%(x,5))

# set x equal to function
x = func1
# call the function stored in x
x()

x = func2
print("VALUE OF X BEFORE FUNC2"+str(x))
x()
print("VALUE OF X AFTER FUNC2: %d"%x)

# define array
arr = []
#add 4 to the end of an array
arr.append(4)
# set array to contain 42 and 3
arr = [42,3]
print(arr)


# see length of array
print(len(arr))

# access each element of array
for el in arr:
    print(x)

# Loop:
i = 0
while i < 5:
    print(i)
    i+=1

# if/else 
if i > 3:
    print("LARGE")
elif i<0:
    print("NEGATIVE")
else:
    print("SMALL")


i = 0
while i<6:
    if i==2:
        #end loop early
        break
print(i)

# will do i = 0 then 1 then 2 ... and then 5 (at 6 stops)
for i in range(6):
    if i%2 ==0:
        # don't do rest of loop and just restart it
        continue
    print("ODD!")

# sort array
arr.sort()

# import package (library) and use it as np
import numpy as np

# create a an array of elements from 1 to 100 with a skip of 5 (so 1, 6, 11, 16...)
arr = np.arange(1,100,5)
print(arr)

# see shape of array
print(arr.shape)


# make array into 2d array with 4 rows and 5 columns
arr = arr.reshape((4,5))
print(arr)

# rotate array -> columns become rows, rows become columns
arr = np.transpose(arr)
print(arr)

# define class
class Person(object):

    #constructor:
    def __init__(self, name, age, height):
        # class contains attribute name now:
        self.name = name
        # class contains attribute age now:
        self.age = age
        # class contains attribute visochina now:
        self.visochina = height

    # define function for class (ALWAYS PASS self AS FIRST PARAMETER)
    def height_v_metri(self):
        return self.visochina/100
    
    def predstavq(self):
        # Access elements of class
        print(self.name)
        print(self.age)
        print(self.height_v_metri())


# Create instance of class
p1 = Person("Nikolay", 22, 183)
# call its function
p1.predstavq()

# access its attribute
print(p1.name)

p2 = Person("Ime","12b",176)
p2.predstavq()

# make 7 by 6 board of 0s (all ints)
game_board = np.zeros((7,6), dtype=np.int32)

# get user value
choice = input("ENTER VALUE: ")

# try to interpret user input as integer
try:
    choice= int(choice)
    if choice == 3:
        print("YOu ARE CORRECT")
except ValueError:
    print("INPUT INTEGER")