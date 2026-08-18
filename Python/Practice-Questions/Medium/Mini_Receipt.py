"""
6. Mini Receipt

Ask the user for:

Product name
Price
Quantity

Then generate a small receipt:

Product: Laptop
Price: 50000
Quantity: 2
Total: 100000

But there's a twist:

The user might enter the product name as:

   LAPTOP

Your final receipt should display:

Product: Laptop

Think about how you can clean and format the input.

Approch :
         Ask user details
            |
         convert the product name to title case and price to float and quantity to integer
            |
         cal the total price (price * quantity)
            |
         Display the details and total price
"""

product_name = input("Enter Product Name :").strip().title()
price = float(input("Enter Price of Product :"))
quantity = int(input("Enter Quantity of Product :"))

total_price = price * quantity

print(f"Product : {product_name}")
print(f"Price : {price}")
print(f"Quantity : {quantity}")
print(f"Total : {total_price}")