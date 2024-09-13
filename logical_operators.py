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
