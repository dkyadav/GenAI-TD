from modules_assignment.math_utils import square, add, subtract
print(add(1,2))
print(subtract(2,1))
print(square(2))

from modules_assignment.string_utils import capitalize_words, reverse_string, word_count
print(capitalize_words("hello world"))
print(reverse_string("hello world"))
print(word_count("hello world"))

# import directly from shop_package as its in __init__.py
from modules_assignment import apply_discount, flat_discount
print(apply_discount(1000, 10))
print(flat_discount(100))

from modules_assignment.shop_package.billing import calculate_total, apply_tax
print(calculate_total([100, 200, 300]))
print(apply_tax(100))
