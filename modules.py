#Mosule is a file with some python code
#we use modules to organize our code into files
import converters
import utils
#importing specific functions from that module
from converters import kg_to_lbs
from utils import find_max

#we can directly call the function without prefixing module name
kg_to_lbs(75)

#used the import statement only; the code is long
print(converters.kg_to_lbs(70))

#find_max([1,2,8,4,5,6])
#utils.find_max([9,8,7,6,5,6,7])
numbers = [34,56,76,56,76,43,93]
max_no = find_max(numbers)
print(max_no)