'''
Reminder: Whenever we define parameters, we should always supply values or
positional arguments. The order matters
'''
from strings import first_name, last_name


def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard')


print("Start")
#specifying with keyword arguments, position doesn't matter
#don't mix keyword arguments with positional arguments
greet_user(last_name="Daniel", first_name="Jacky")
#you can add keyword argument after positional argument
greet_user("Johnny", last_name="Smithy")
print("Finish")