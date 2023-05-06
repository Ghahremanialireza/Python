### USER INPUT
# how do we accept user inputs and do calculation etc.
#     input()
# This is a function we can use it whenever we want ...
# This is a Built-in function in python
# we can use \n to go to next line
#use int() to change data type to integer
def Calculator (x,y):
    print(f" {x} * {y} = {int(x) * int(y)}")
    print(f" {x} + {y} = {int(x) + int(y)}")
    print(f" {x} - {y} = {int(x) - int(y)}")
    print(f" {x} / {y} = {int(x) / int(y)}")

x = input("firstnumber: ")
y = input("second number: ")
Calculator(x,y)



### Funcion with return values
# if we want a value that is result of function we use return
# return ()

def returnfunction(old):
    return print(f"{int(old)*3}")
old = input("How old are u???")
returnfunction(old)