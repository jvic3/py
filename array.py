courses = ["MIT","Cybersecurity","Datascience"]
print(courses)


# Accessing an element in array
print(courses[1])

# Looping through array
for course in courses:
    print(course)

# Adding an element into an array
courses.append("Android Development")
print(courses)



# Deleting an element from an array
courses.remove("Datascience")
print(courses)
