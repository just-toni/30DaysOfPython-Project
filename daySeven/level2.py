# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# 1
C = A.union(B)
print(C)

# 2
print(A.intersection(B))

# 3
print(A.issubset(B))

# 4
print(A.isdisjoint(B))
print(B.isdisjoint(B))

# 5
D = B.union(A)

# 6
print(A.symmetric_difference(B))

# 7
del A
del B

