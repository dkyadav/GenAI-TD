import math_utils
from math_utils import square

print(math_utils.add(1,2))
print(math_utils.subtract(2,1))
print(math_utils.square(2))
print(square(2))

import string_utils
print(string_utils.capitalize_words("hello world"))
print(string_utils.reverse_string("hello world"))
print(string_utils.word_count("hello world"))

from shop_package.discount import apply_discount, flat_discount
print(apply_discount(1000, 10))
print(flat_discount(100))

from shop_package.billing import calculate_total, apply_tax
print(calculate_total([100, 200, 300]))
print(apply_tax(100))
