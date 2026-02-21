#Task 1.1 create a list named products with 10 product names
products = ["laptop", "mouse", "keyboard", "pen", "book", "notebook", "jeans", "shirt", "sharpener", "ruler"]

#Task 1.2 create a tupple named sample_product that stores (product_name, price, category)
sample_product = ("laptop", 100, "electronics")

#Task1.3
print(products[1], products[len(products)-1]);

#Task1.4
products.append("calculator")
products.append("marker")
print(products)

#Task1 Extra convert sample_product to a list
sample_product_list = list(sample_product)
sample_product_list[1] = 200
sample_product_updated_tupple = tuple(sample_product_list)
print(sample_product_updated_tupple)

#Task 2.1 From products list create a set of categories called categories_set
categories_set = set()
for product in products:
    categories_set.add(product)
print(categories_set)

#Task 2.2
categories_set.add("cloth")
print(categories_set)
categories_set.add("cloth")
print(categories_set)

#Task 2.3 check if category exists within categories_set
print("cloth" in categories_set)
if("cloth" in categories_set):
    print("cloth exists in categories_set")

print("games" in categories_set)
if("games" in categories_set):
    print("games exists in categories_set")
else:
    print("games does not exist in categories_set")

#Task 2 Extra
print(f"Total number of unique categories: {len(categories_set)}")

#Task 3.1
price_dict = {}
i=1
for product in products:
    price_dict[product] = float(100*i)
    i+=1
print(price_dict)

#Task 3.2
price_dict.update({"new_product": 150.0})
print(price_dict)   
price_dict.update({"new_product": 250.0})
print(price_dict)
price_dict.pop("new_product")
print(price_dict)
price_dict.pop("new_product", None)
print(price_dict)

#Task 3.3
print(f"Average price of all products: {sum(price_dict.values()) / len(price_dict)}")

#Task 3 Extra
min_price = min(price_dict.values())
max_price = max(price_dict.values())
print(f"Product of min: {min_price} and max: {max_price} price: {min_price * max_price}")

#Task 4.1 using products list and price_dict, creata a list of tuples named catalog where each tuple is (product_name, price, category)
catalog = []
for product in products:
    #product is any one "laptop", "mouse", "keyboard", "pen", "book", "notebook"
    if(product in ["laptop", "mouse", "keyboard"]):
        cat = 'Electronics'
    elif(product in ["jeans", "shirt"]):
        cat = 'Cloth'
    else:
        #else category is "Stationary"
        cat = 'Stationary'
    catalog.append((product, price_dict[product], cat))
print(catalog)

#Taks 4.2 catalog list to a dictionary
cataory_to_products = {}
for product, price, category in catalog:
    if category not in cataory_to_products:
        cataory_to_products[category] = []
    cataory_to_products[category].append(product)
print(cataory_to_products)

#Task 4.3
cat_with_count = {}
for cat_key,cat_val in cataory_to_products.items():
    print(f"Category: {cat_key}, Products: {cat_val}")
    temp_add = {
        cat_key: len(cat_val)
    }
    cat_with_count.update(temp_add)

#find key with max value
max_key = max(cat_with_count, key=cat_with_count.get)
print(f"Category with most products: {max_key} have {cat_with_count[max_key]} products: {cataory_to_products[max_key]}")
