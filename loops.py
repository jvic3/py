# while loop
# increment
number = 5
while number <= 10:
    print(number)
    number += 1


# decrement
num = 105
while num >= 100:
    print(num)
    num -= 1

# break statement
x = 20
while x <= 25:
    print(x)
    if x == 24:
        break
    x += 1

# continue statement
y = 79
while y < 85:
    y += 1
    if y == 83:
         continue

    print(y)

# For loop
languages = ["Python","Java","C++"]
for z in languages:
    print(z)


# range
for mynumber in range(5):
    print(mynumber)

for mynum in range (2,5):
    print(mynum)

for count in range(20,30,2):
    print(count)
