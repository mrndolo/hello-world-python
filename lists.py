names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
print(names[0])
print(names[-1])
#colon to select range of items(index 4 is not returned)
print(names[2:4])
#default values(if you leave out the end index, will display till the end of the list)
print(names[2:])
#default values(if you leave out the start index, will assume 0 as the default index)
print(names[:3])
names[0] = 'Johnson'
print(names)

#program to find the largest number in a list
numbers = [1,2,3,4,5,9]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)