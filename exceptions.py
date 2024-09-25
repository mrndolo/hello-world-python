#we use try except blocks to handle exceptions that are raised in our programs
try:
    age = int(input('Age: '))
    income = 2000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Age cannot be 0')
except ValueError:
    print('Invalid value')

#exit code 0 = program terminated successfully with no errors
#ValueError: string instead of a float
