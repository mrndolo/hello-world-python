numbers = [5,2,1,7,4,4]
#add a new item to the list
numbers.append(20)
print(numbers)
numbers.insert(0, 10)
print(numbers)
numbers.remove(5)
print(numbers)
#return index of the first occurrence of the item
print(numbers.index(7))
#check existence of value in list
print(4 in numbers)
#count occurrence of an item in the list
print(numbers.count(4))
#sort items in a list; ascending order
numbers.sort()
print(numbers)
#sort in descending order
numbers.reverse()
print(numbers)
#get a copy of the list
numbers2 = numbers.copy()
print(numbers2)

#program to remove the duplicates in the list
numbers3 = [1,2,3,4,5,6,6,6]
uniques = []
for number in numbers3:
    if number not in uniques:
        uniques.append(number)
print(uniques)
