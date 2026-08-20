"""
2. Round the Price

Ask the user for the price of a product.

The user might enter:

Enter price: 149.678

Your program should display:

Original price: 149.678
Rounded price: 149.68

The rounded price must have exactly 2 decimal places.

"""

product_price = float(input("Enter The Product Price :"))

rounded_price = round(product_price,2)

print(f"Original price: {product_price}")
print(f"Rounded price : {rounded_price:.2f}")