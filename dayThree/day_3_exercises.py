# 1
age = 20

# 2
height = 1.8034

# 3
variable = 7j

# 4
base = float(input("Enter base: "))
height1 = float(input("Enter height: "))
print("The area of the triangle is ", 0.5 * base * height1)

# 5
side_a = float(input("Enter side a: "))
side_b = float(input("Enter side b: "))
side_c = float(input("Enter side c: "))
print("The perimeter of the triangle is ", side_a + side_b + side_c)

# 6
length = float(input("Enter base: "))
width = float(input("Enter height: "))
print("The area of the rectangle is ", length * width)
print("The perimeter of the rectangle is ", 2 * (length + width))

# 7
radius = float(input("Enter radius: "))
print("The area of the circle is ", radius ** 2 * 3.14)
print("The perimeter of the circle is ", 2 * radius * 3.14)

# 8
y1 = (2 * 0) - 2
y2 = 0
x1 = 1
x2 = 0
slope1 = (y2 - y1) / (x2 - x1)
print("This is the slope for the x-intercept (1,0) and y-intercept (-2, 0)", slope1)

# 9
y1 = 2
y2 = 10
x1 = 2
x2 = 6
slope2 = (y2 - y1) / (x2 - x1)
euclidean_distance = 7  # find proper formula for this and fix it
print("This is the slope for the x-intercept (2, 6) and y-intercept (2, 10)", slope2)

# 10
print("Is slope1 greater than slope2? ", slope1 > slope2)
print("Is slope2 greater than slope1? ", slope1 < slope2)

# 11 skipped

# 12
print("Word length of python is", len('python'))
print("Word length of dragon is", len('dragon'))
print("Word length for dragon is more than python", len('dragon') < len('python'))

# 13
print("The word 'on' is found in Python and Dragon", 'on' in 'Python' and 'on' in 'Dragon')

# 14
print("Word jargon is present ", 'jargon' in 'I hope this course is not full of jargon')

# 15
print("The word 'on' is not found in Python and Dragon", not('on' in 'Python' and 'on' in 'Dragon'))

# 16
print('Word length for python is ', len('python'))
print('Word length for python in float format is ', float(len('python')))
print('Word length for python in a string format is ', str((len('python'))))

# 17
num = int(input("Enter a number to check if it is even or odd: "))
print(num, "is even ", num % 2 == 0)

# 18
print('Is 7/3 equal to 2 using integer division', 7//3 == int(2.7))

# 19
print('"10" equal to 10', '10' == 10)

# 20
print('int(9.8) equal to 10', int(9.8) == 10)

# 21
hours = float(input("Enter hours: "))
rate = float(input("Enter rate per hour: "))
print("Your weekly earning is ", hours * rate)

# 22
years = float(input("Enter number of years you have lived: "))
print("You have lived for ", years * 31536000, 'seconds')

# 23
print(1, 1**0, 1**1, 1**2, 1**3)
print(2, 2**0, 2**1, 2**2, 2**3)
print(3, 3**0, 3**1, 3**2, 3**3)
print(4, 4**0, 4**1, 4**2, 4**3)
print(5, 5**0, 5**1, 5**2, 5**3)
