# Data Types
number = 45 # integars
bun = 56.78 # float
greeting = "Hello there" # str
isPythonInteresting = True # bool


# Variable storing multiple values
language = ["python","php","java"] # List
fruits = ("apple","banana","pineapple") # Tuple
countries = {"Kenya","China","USA"} # set

# Dictionary
details = {
    "firstname" : "Grace",
    "age" : 17,
    "course" : "MIT",
    "nationality" : "North America"

}

print(details["course"])
print(details["nationality"])
print(details)
print(number)
print(greeting)
print(countries)
print(isPythonInteresting)


# Determining the data type
print(type(details))
print(type(countries))

# Type casting - converting one data type to another
print(float(number))
print(int(bun))
