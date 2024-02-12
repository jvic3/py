try:
    print(x)
except:
    print("NameError occured")
finally:
    print("Success")


num1 = 20
num2 = 0
try:
    print(num1 / num2)
except:
    print("ZeroDivisionError occured")


# User - define function
try:
 def multiply(x, y):
    return x * y
except:
    print("Exception occured")
finally:
    print("Success")

print(multiply(10,20))
