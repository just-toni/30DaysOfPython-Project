# 1
new_list = []
new_list_1 = list()

# 2
songs = ['Found A Love', 'Broken', 'Praises', 'Kadosh', 'To See You', 'Wonderful', 'Millionaire (Good Like That)']

# 3
print('Number of songs is', len(songs))

# 4
print('First item:', songs[0])
print('Middle item:', songs[len(songs) // 2])
print('Last item:', songs[-1])

# 5
mixed_data_types = ['Toni', 20, '5\'11', 'single', 'Canada']

# 6
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7
print(mixed_data_types)

# 8
print(it_companies)

# 9
print('First item:', it_companies[0])
print('Middle item:', it_companies[len(it_companies) // 2])
print('Last item:', it_companies[-1])

# 10
it_companies = ['Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)

# 11
it_companies = ['Facebook', 'SAP', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 12
it_companies.insert(len(it_companies) // 2, 'Cognizant')

# 13
it_companies[2] = it_companies[2].upper()

# 14
it_companies.extend('#')
print(it_companies)

# 15
print('Pepsi' in it_companies)

# 16
it_companies.sort()
print(it_companies)

# 17
it_companies.reverse()
print(it_companies)

# 18
new_list = it_companies[3:]
print(new_list)

# 19
new_list = it_companies[:len(it_companies) - 3]
print(new_list)

# 20
print(it_companies)
it_companies = it_companies[:len(it_companies) // 2] + it_companies[len(it_companies) // 2 + 1:]
print(it_companies)

# 21
it_companies.pop(0)
print(it_companies)

# 22
it_companies.pop(len(it_companies) // 2)
print(it_companies)

# 23
it_companies.pop(-1)
print(it_companies)

# 24
it_companies.pop()
it_companies.pop()
it_companies.pop()
it_companies.pop()
it_companies.pop()
it_companies.pop()
print(it_companies)

# 25
del it_companies

# 26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
new_list_1 = front_end + back_end
print(new_list_1)

# 27
full_stack = new_list_1.copy()
print(full_stack)
indx = full_stack.index('Redux')
full_stack.insert(indx+1, 'Python')
full_stack.insert(indx+2, 'SQL')
print(full_stack)
