# 1
dog = {}
dog_1 = dict()

# 2
dog["name"] = "Billy"
dog['color'] = "white"
dog['breed'] = 'German Shepard'
dog['legs'] = 4
dog['age'] = 1

# 3
student_dictionary = {
    "first_name": "Toni",
    "last_name": "Adeniyi",
    "gender": "F",
    "age": 20,
    "martial status": "Single",
    "skills": ['Java', 'Python', 'JS', 'Node', 'HTML/CSS', 'PHP'],
    "country": "Canada",
    "city": "Halifax",
    "address" :{
        "street": "North End Halifax",
        "postal_code": "A1B2C3",
    },
}

# 4
print(len(student_dictionary))

# 5
print(student_dictionary.values())
print(type(student_dictionary))

# 6
student_dictionary['skills'].append('Photography')
print(student_dictionary['skills'])

# 7
print(student_dictionary.keys())

# 8
print(student_dictionary.values())

# 9
print(student_dictionary.items())

# 10
del student_dictionary['address']
print(student_dictionary)

# 11
del student_dictionary
