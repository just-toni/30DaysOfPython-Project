import level1
# 1
*siblings, father, mother = level1.family_members

# 2
fruits = ('Watermelon', 'Apple', 'Pineapple', 'Mango', 'Grapes')
veggies = ('Broccoli', 'Onions', 'Brussel Sprouts')
animal_products = ('Milk', 'Eggs', 'Goat meat', 'Bacon')

food_stuff_tp = fruits + veggies + animal_products

# 3
food_stuff_list = food_stuff_tp

# 4
food_stuff_list = food_stuff_list[:len(food_stuff_list)//2] + food_stuff_list[len(food_stuff_list)//2 + 1:]
print(food_stuff_list)

# 5
food_stuff_list = food_stuff_list[3:len(food_stuff_list)-3]
print(food_stuff_list)

# 6
del food_stuff_list

# 7
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
