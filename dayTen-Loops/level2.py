# 1
sum=0
for i in range(0, 100):
    sum+=i
print("The sum of all numbers is", sum)

# 2
sum_even=0
sum_odd=0
for i in range(0, 100):
    if i%2==0 : sum_even+=i
    else: sum_odd+=i
print("The sum of all even numbers is", sum_even)
print("The sum of all odd numbers is", sum_odd)