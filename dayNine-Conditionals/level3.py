# 1
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

#  * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
#  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
#  * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has
#  Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB,
#  Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions
#  can be nested!
#  * If the person is married and if he lives in Finland, print the information in the following format:

if person.get('skills'):
    print(person['skills'][len(person['skills']) // 2])
if 'Python' in person['skills']:
    print(True)
else:
    print(False)
if person['skills'] == ['JavaScript', 'React']:
    print('He is a front end developer')
elif person['skills'] == ['Node', 'Python', 'MongoDB']:
    print('He is a backend developer')
elif person['skills'] == ['React', 'Node', 'MongoDB']:
    print('He is a fullstack developer')
else:
    print('Unknown title')
if person['is_marred'] == True and person['country'] == 'Finland':
    print(person['first_name'], person['last_name'], 'lives in', person['country'], '. He is married')
