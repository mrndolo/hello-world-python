#passing information to your functions
#Inside the parenthesis we can add parameters(placeholders for receiving information)
#NB: when a function has a parameter, we are obligated to pass a value for that parameter
#argument is the value that we supply to a function
def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard')


print("Start")
greet_user("John", "legend")
greet_user("Jack", "Daniel")
print("Finish")