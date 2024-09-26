#A way to organize our code
#A package is a container for multiple modules(a directory or folder)
# importing entire module
import ecommerce.shipping
# Very verbose method of calling functions
ecommerce.shipping.calc_shipping()

# Use this second approach instead to shorten function calls
from ecommerce.shipping import calc_shipping

calc_shipping()

# Use this to import multiple functions of entire module
from ecommerce import shipping
shipping.calc_shipping()

