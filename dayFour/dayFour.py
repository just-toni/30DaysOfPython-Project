# 1
import math

str_one = 'Thirty'
str_two = 'Days'
str_three = 'Of'
str_four= 'Python'

print(str_one + " " + str_two + " " + str_three + " " + str_four)

# 2
str_one = 'Coding'
str_two = 'For'
str_three = 'All'
print(str_one + " " + str_two + " " + str_three)

# 3
company = "Coding For All"

# 4
print(company)

# 5
print("Length of", company, "is", len(company))

# 6
print(company.upper())

# 7
print(company.lower())

# 8
print(company.capitalize())
print(company.title())
print(company.swapcase())

# 9
print(slice(company))

# 10
print(company.find('Coding'))
print(company.index('Coding'))

# 11
print(company.replace('Coding', 'Python'))

# 12
print(company.replace('All', 'Everyone'))

# 13
print(company.split(' '))

# 14
str1 = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(str1.split(','))

# 15
print(company[0])

# 16
print(company[-1])

# 17
print(company[10])

# 18
str2 = 'Python For Everyone'.split()
print(str2[0][0], str2[1][0], str2[2][0])

# 19
str2 = 'Coding For All'.split()
print(str2[0][0], str2[1][0], str2[2][0])

# 20
print(company.index('C'))

# 21
print(company.index('F'))

# 22
print(company.join('People').rfind('I'))

# 23
str2 = 'You cannot end a sentence with because because because is a conjunction'
print(str2.find('because'))

# 24
print(str2.rindex('because'))

# 26
print(str2.find('because'))

# 25 / 27
print(str2.replace('because because because', ''))

# 28
print(company.startswith('Coding'))

# 29
print(company.endswith('Coding'))

# 30
str2 = '   Coding For All      '
print(str2.strip(' '))

# 31
str1 = '30DaysOfPython'
str2 = 'thirty_days_of_python'
print(str1.isidentifier())
print(str2.isidentifier())

# 32
print('-'.join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']))

# 33
print("I am enjoying this challenge. \nI just wonder what is next.")

# 34
print('Name\tAge\tCountry\tCity')
print('Toni\t20\tCanada\tHalifax')

# 35
radius = 10
area = math.pi * radius ** 2
print('The area of a circle with radius {} is {:1f} meters square'.format(radius, area))

# 36
a, b = 8, 6
print('{} + {} = {}'.format(a, b, a+b))
print('{} - {} = {}'.format(a, b, a-b))
print('{} * {} = {}'.format(a, b, a*b))
print('{} / {} = {:.2f}'.format(a, b, a/b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a//b))
print('{} ** {} = {}'.format(a, b, a**b))
