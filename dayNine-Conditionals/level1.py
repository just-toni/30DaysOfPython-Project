# 1
your_age = int(input('Enter your age:'))
if your_age > 18:
    print('You are old enough to drive')
else:
    print('You need to wait {} years'.format(18 - your_age))

# 2
my_age = 20
if my_age > your_age:
    print('Your are {} years younger than me'.format(my_age - your_age))
elif my_age < your_age:
    print('Your are {} years older than me'.format(your_age - my_age))
else:
    print("We are the same age!")

# 3
num1 = int(input("Enter number one: "))
num2 = int(input("Enter number two: "))
if num1 > num2:
    print('{} is greater than {}'.format(num1, num2))
elif num1 < num2:
    print('{} is greater than {}'.format(num2, num1))
else:
    print("They are the same number")
