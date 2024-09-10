course = "Python for Beginners"
course2 = 'Python for "Beginners"'

multiple_line_strings = '''
Hi Carl.
Here is our first project
'''

print(course[0])
print(course[-1])
print(course[0:3])
print(course[0:])
print(course[1:])
print(course[:5])
#copy or clone a string
print(course[:])
another = course[:]
print(another)

name = 'Jennifer'
print(name[1:-1])

#formatted strings
first_name = 'John'
last_name = 'Smith'

#John [Smith] is a coder
message = first_name + ' [' + last_name + '] is a coder'
print(message)
#formattes string
msg = f'{first_name} [{last_name}] is a coder'
print(msg)

#string methods
print(len(course))
change = course.upper()
print(change)
print(course.find('P'))
print(course.replace('Beginners', 'Absolute Beginners'))
print('Python' in course)
