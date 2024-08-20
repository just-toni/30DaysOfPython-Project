import data.countries as countries
import data.countries_data as countries_data

# 1
for country in countries.countries:
    if 'land' in country:
        print(country)

# 2
fruits = ['banana', 'orange', 'mango', 'lemon']
for fruit in range(len(fruits) - 1, -1, -1):
  print(fruits[fruit])

# 3
# i
sum = 0
for i in range(len(countries_data.countries_data)):
    sum+=len(countries_data.countries_data[i]['languages'])
    # print (countries_data.countries_data[i]['languages'])
print(sum)

# ii
allLanguages = []
for i in range(len(countries_data.countries_data)):
    allLanguages.append(countries_data.countries_data[i]['languages'])
print(allLanguages)
