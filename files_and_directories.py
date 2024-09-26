# Pathlib module - provides an object oriented file system pact
# It provides classes that we can use to create objects to work with directories and files

from pathlib import Path
# Absolute path(start from the root of our hard disk)
# Relative path(path starting form the current directory)

# path = Path("emails")
# print(path.exists())
# print(path.mkdir())
# print(path.rmdir())

# Find all the files and directories in a given path
path = Path()
print(path.glob('*.py'))
#all python files in current directory
for file in path.glob('*.py'):
    print(file)
print('*='*10)


#all files and directories within our program
for file in path.glob('*'):
    print(file)

