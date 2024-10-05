def outer():
    x = 10
def inner():
      # Error: x is local to outer and cannot be made global
    x = 5
    return x
x=inner()
print(x)

outer()
