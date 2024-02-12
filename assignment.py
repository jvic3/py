# a program to calculate using operators
x = float(input("Enter first number:"))
y = float(input("Enter second number"))
operator = input("Enter operator:")
if operator == "+":
    print("result is : ",x+y)
elif operator == "-":
    print("result is : ", x - y)
elif operator == "*":
    print("result is : ", x * y)

elif operator == "/":
    print("result is : ", x / y)
else: print("invalid operator")
