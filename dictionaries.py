#when we want to store information as key value pairs
'''
for example...
Name: John Smith
Email: John@gmail.com
Phone: 1234
the keys should be unique
'''
customer = {
    "name": "John Smith",
    "Email": "john@gmail.com",
    "phone": 1234,
    "age": 30,
    "is_verified": True
}
print(customer["name"])
#will return none because it does not exist
print(customer.get("birthdate"))
#return a default value
print(customer.get("birthdate", "Jan 1 1980"))
#updating a dictionary value
customer["name"] = "Jack Daniel"
print(customer["name"])
#add a new key
customer["birthdate"] = "Jan 1 2000"
print(customer["birthdate"])

#program that translates numbers to digits
phone = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)