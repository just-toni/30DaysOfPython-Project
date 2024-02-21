# 1
empty_tuple = ()

# 2
brothers = ('Ben', 'Jerry', 'Fred')
sisters = ('Mollie', 'Jenny')

# 3
siblings = brothers + sisters

# 4
print(len(siblings))

# 5
family_members = siblings + ('Mom', 'Dad')
*siblings, dad, mum = family_members
print(siblings)
print(dad)
print(mum)

