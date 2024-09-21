#matrix - rectangular array of numbers
#2d list - each item in that list is another list
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
matrix[0][1]=20
print(matrix[0][1])

#using nested loops to iterate over all the items in the list
for row in matrix:
    for item in row:
        print(item)