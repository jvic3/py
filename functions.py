# Inbuilt functions
number = max(89,70,60,45,123)
print(number)

x = min(78,45,60,89,78)
print(x)

z = pow(2,3)
print(z)

# User-defined functions
def name():
    print("June")

name() # Calling a function

def student():
    name = "Vincent"
    age = 18
    course = "MIT"
    print(name,age,course)

student()

# Parameters/variables and arguments/values

def student(name,age,course):
    print(name,age,course)

student("Joy",18,"Cybersecurity")
student("Jane",16,"Fullstack")
student("Paul",18,"MIT")
student("James",17,"MIT")


# Create a user-defined function
def employees(name, age, gender, position, salary):
    print(name, age, gender, position, salary)

employees("Joy Jane",34,"female","manager",90,000)
employees("James John",38,"male","CEO",190,000)
employees("Paul Kim",40,"male","Secretary",70,000)
employees("Amos Job",30,"male","Organisor",60,000)
employees("Simon Kimali",35,"male","planner",80,000)


