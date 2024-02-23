# 1
grade = int(input('Enter your grade: '))
if 80 < grade <= 100:
    print('A')
elif 80 < grade <= 70:
    print('B')
elif 70 < grade <= 60:
    print('C')
elif grade < 60 and grade <= 50:
    print('D')
else:
    print('F')

# 2
month = input('Enter any month of your choice: ')
if month == 'January' or 'February' or 'December':
    print('Winter')
elif month == 'March' or 'May' or 'June':
    print('Spring')
elif month == 'July' or 'August' or 'September':
    print('Summer')
else:
    print('Autumn')

# 3
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input('Enter a fruit of your choice')
if fruit not in fruits:
    fruits.append(fruit)
    print(fruit, 'has been added to the Fruits list')
else:
    print(fruit, 'is already present in the Fruits list')
