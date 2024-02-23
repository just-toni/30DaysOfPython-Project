# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

# 1
print(len(it_companies))

# 2
it_companies.add('Twitter')
print(it_companies)

# 3
it_companies.update(['Cognizant', 'LinkedIn', 'Tesla'])
print(it_companies)

# 4
it_companies.pop()
print(it_companies)

# 5
it_companies.remove('LinkedIn')
print(it_companies)
it_companies.discard('IBM')
print(it_companies)
