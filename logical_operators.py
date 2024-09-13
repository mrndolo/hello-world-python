'''
if an applicant has high income AND good credit
    eligible for loan
if applicant has good credit and doesn't have a criminal record
    eligible for loan

    AND: both
    OR: at least one
    NOT: inverts boolean value
'''

has_high_income = True
has_good_credit = True
has_criminal_record = False

if has_high_income and has_good_credit:
    print("Eligible for loan")

if has_high_income or has_good_credit:
    print("Eligible for loan-ish")

if has_good_credit and not has_criminal_record:
    print("Eligible for loan")

#comparison operators
'''
if temperature id grater than 30
    it's a hot day
otherwise if it's less than 10
    it's a cold day
otherwise
    it's neither hot nor cold
'''
temperature = 30

if temperature >= 30:
    print("It's a hot day")
else:
    print("It's not a hot day")

'''
if name is less than 3 characters long
    name must be at least 3 characters
otherwise if it's more than 50 characters long
    name can be a maximum of 50 characters
otherwise
    name looks good!
'''
name = "John"

if len(name) < 3:
    print("name must be at least 3 characters")
elif len(name) > 50:
    print("Name can be a maximum of 50 characters")
else:
    print("Looks good!")