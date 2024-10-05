none = "some_value"
if none == "some_value":
    print("This shouldn't work, None is a keyword!")
true = 1
if true: 
    print("This will cause an error because 'True' is a reserved keyword.")

def For(x):
    return x * 2

result = For(5)
print(result)  

if result > 5:
    print("You can't use 'return' as a variable name!")

Class = "AdvancedPython"
print("This won't work because 'class' is a reserved keyword in Python.")

