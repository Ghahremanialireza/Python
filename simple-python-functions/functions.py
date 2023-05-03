### FUNCTIONS
# we use functions to avoid duplication
# instead of typing a code many times we use function

# a code without using function

calculation = 365 * 24 * 60 * 60

print(f"if i have 20 years old it means i have lived {20 * calculation }  seconds")
print(f"if i have 25 years old it means i have lived {25 * calculation }  seconds")
print(f"if i have 33 years old it means i have lived {33 * calculation }  seconds")
print(f"if i have 50 years old it means i have lived {50 * calculation }  seconds")


# code using function
def sec_calculator():
    calculation = 365 * 24 * 60 * 60
    print(f"if i have 20 years old it means i have lived {20 * calculation}  seconds")

# after defining function we call that like this
sec_calculator()

# use function parameters
def sec_calculator(age):
    calculation = 365 * 24 * 60 * 60
    print(f"if i have {age} years old it means i have lived {age * calculation}  seconds")

# after defining function we call that like this
sec_calculator(18)
sec_calculator(22)

# we can simply change a var name in def function instead of changin whole code
# Note : we can use several input function
def sec_calculator(age,message):
    calculation = 365 * 24 * 60 * 60
    print(f"if i have {age} years old it means i have lived {age * calculation}  seconds")
    print(message)

sec_calculator(age,message)


### variable SCOPES in fucntions
# local variables : created in function and can be used just in that function
# global variable : we can use it in all code
