#iterate over items of a collection such as a string
# item is the loop variable
for item in 'Python':
    print(item)

for item in ['John', 'Doe', 'Mark', 'Sarah']:
    print(item)

for item in [1,2,3,4,5]:
    print(item)

#for long lists, we ise range
for item in range(10):
    print(item)

#calculate the cost of all items in a shopping cart
prices = [10,20,30]

total = 0
for price in prices:
    total += price
print(f"Total: {total}")