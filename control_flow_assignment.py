#Task1
try:
    order_amount = int(input("Enter order amount:"))
    discount = 0
    if(order_amount >= 2000):
        print("Discount is 15%")
        discount = 0.15
    elif(order_amount >= 1500):
        print("Discount is 10%")
        discount = 0.10
    elif(order_amount >= 1000):
        print("Discount is 7%")
        discount = 0.07
    else:
        print("Discount is 0%")

    #Task1 extra
    fixed_tax = 0.05
    discount_amount = order_amount * (1-discount)
    tax_amount = discount_amount * (1+fixed_tax)    
    print(f"Final total after 5% tax and discount of {round(discount*100,1)}%: ", round(tax_amount,2))
except ValueError:
    print("Invalid order amount, enter numeric value")
except Exception as e:
    print("An error occurred:", e)  


#Task2
orders = [1200, 2500, 800, 1750, 3000]
order_with_discount = 0

for order_amount in orders:
    discount = 0
    if(order_amount >= 2000):
        discount = 0.15
        order_with_discount+=1
    elif(order_amount >= 1500):
        discount = 0.10
        order_with_discount+=1
    elif(order_amount >= 1000):
        discount = 0.07
        order_with_discount+=1
    
    #Task1 extra
    fixed_tax = 0.05
    discount_amount = order_amount * (1-discount)
    tax_amount = discount_amount * (1+fixed_tax)    
    print(f"order_amount: {order_amount}, discount: {round(discount*100,1)}% -> final_amount: {round(tax_amount,2)}")
    print(f"number of orders that received a discount: {order_with_discount}")


#Task3: while-loop driven menu that keeps asking the user to choose an action until they press q to quit.
all_orders = []
while True:
    print("\n=== MENU ===")
    print("1. Add order amount to a running list")
    print("2. Show all ordesr and totals after applying discounts")
    print("q. Quit")
    
    choice = input("Enter your choice (1/2/q): ").lower().strip()

    if choice == 'q':
        print("Goodbye!")
        break
    elif choice == '1':
        try:
            order_amount = int(input("Enter order amount: "))
            discount = 0
            if order_amount >= 2000:
                print("Discount is 15%")
                discount = 0.15
            elif order_amount >= 1500:
                print("Discount is 10%")
                discount = 0.10
            elif order_amount >= 1000:
                print("Discount is 7%")
                discount = 0.07
            else:
                print("Discount is 0%")
            
            fixed_tax = 0.05
            discount_amount = order_amount * (1-discount)
            tax_amount = discount_amount * (1+fixed_tax)
            print(f"Final total after 5% tax and discount of {round(discount*100,1)}%: {round(tax_amount,2)}")
            all_orders.append(f"order_amount: {order_amount}, discount: {round(discount*100,1)}% -> final_amount: {round(tax_amount,2)}")
        except ValueError:
            print("Invalid order amount, enter numeric value")
        except Exception as e:
            print("An error occurred:", e)
    
    elif choice == '2':
        for order in all_orders:
            print(order)
    
    else:
        print("Invalid choice. Please try again.")


#Task4 -> missing

#Task5
daily = [200, 150, 0, 400, 50, -1, 300]
total_sales = 0
corrupted_data = False
for sales in daily:
    print(sales)
    if int(sales) < 0:
        print("corrupted data")
        corrupted_data = True
        break
    elif int(sales) == 0:
        print("No sales")
        continue
    else:
        total_sales += int(sales)
    
print(f"Total sales, corrupted data found {corrupted_data} => {total_sales}")
    