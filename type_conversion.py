#input always gives a string value
birth_year = input('Birth year: ')
print(type(birth_year))
age = 2024 - int(birth_year)
print(type(age))

print(age)

weight_pounds = input('What is your weight in pounds? ')
to_pounds = int(weight_pounds) / 2.205
print('You are ' + str(to_pounds) + ' Kg')
