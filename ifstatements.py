'''
if it's hot
    It's a hot day
    Drink plenty of water
otherwise if it's cold
    It's a cold day
    Wear warm clothes
otherwise
    It's a lovely day
'''

is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("its a lovely day")

print("Enjoy your day")


'''
Price of a house is $1M.
If buyer has good credit,
they need to put down 10%
Otherwise
they need to put down 20%
Print the down payment
'''

house_price = 1000000
has_good_credit = False

if has_good_credit:
    down_payment = house_price * 0.1
else:
    down_payment = house_price * 0.2
print(f"Down payment: ${down_payment}")
