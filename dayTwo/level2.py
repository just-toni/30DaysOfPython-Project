import math

import level1

# 1
type(level1.first_name)
type(level1.last_name)
type(level1.age)
type(level1.country)
type(level1.full_name)
type(level1.city)
type(level1.color)
type(level1.drink)
type(level1.food)
type(level1.is_true)
type(level1.is_married)
type(level1.is_light_on)

# 2
print(len(level1.first_name))

# 3
print(max(len(level1.first_name), len(level1.last_name)))
print(min(len(level1.first_name), len(level1.last_name)))

# 4
num_one, num_two = 5,4
# i
total = num_one + num_two
# ii
diff = num_one - num_two
# iii
product = num_one * num_two
# iv
division = num_one / num_two
# v
remainder = num_one % num_two
# vi
exp = num_one ** num_two
# vii
floor_division = num_one // num_two

# 5
#i
area_of_circle = math.pi * 30**2
print(area_of_circle)
#ii
circum_of_circle = math.pi * 2 * 30
print(circum_of_circle)
#iii
radius = int(input("Enter a radius:"))
area_of_circle = math.pi * radius ** 2
print("Area is ", math.pi * radius ** 2)
print("Circumference is ", math.pi * radius * 2)

#6
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
age = input("What is your age? ")
country = input("What is country are you from? ")

#7
help('keywords')