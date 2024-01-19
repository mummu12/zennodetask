product_a_name = "Product A"
product_a_price = 20
product_a_quantity = int(input(f"Enter quantity of {product_a_name}: "))
product_a_gift_wrap = input(f"Wrap {product_a_name} as a gift? (yes/no): ").lower() == "yes"
product_a_total = product_a_quantity * product_a_price
product_a_discount = product_a_total * 0.05 if product_a_quantity > 10 else 0
product_a_gift_wrap_fee = product_a_quantity if product_a_gift_wrap else 0

product_b_name = "Product B"
product_b_price = 40
product_b_quantity = int(input(f"Enter quantity of {product_b_name}: "))
product_b_gift_wrap = input(f"Wrap {product_b_name} as a gift? (yes/no): ").lower() == "yes"
product_b_total = product_b_quantity * product_b_price
product_b_discount = product_b_total * 0.05 if product_b_quantity > 10 else 0
product_b_gift_wrap_fee = product_b_quantity if product_b_gift_wrap else 0

product_c_name = "Product C"
product_c_price = 50
product_c_quantity = int(input(f"Enter quantity of {product_c_name}: "))
product_c_gift_wrap = input(f"Wrap {product_c_name} as a gift? (yes/no): ").lower() == "yes"
product_c_total = product_c_quantity * product_c_price
product_c_discount = product_c_total * 0.05 if product_c_quantity > 10 else 0
product_c_gift_wrap_fee = product_c_quantity if product_c_gift_wrap else 0

subtotal = product_a_total + product_b_total + product_c_total

bulk_discount = max(product_a_discount, product_b_discount, product_c_discount)
flat_discount = 10 if subtotal > 200 else 0
total_discount = max(bulk_discount, flat_discount)

total_quantity = product_a_quantity + product_b_quantity + product_c_quantity
shipping_fee = (total_quantity // 10) * 5

total_gift_wrap_fee = product_a_gift_wrap_fee + product_b_gift_wrap_fee + product_c_gift_wrap_fee
total_amount = subtotal - total_discount + shipping_fee + total_gift_wrap_fee


print("\nProduct Details:")
print(f"{product_a_name}: {product_a_quantity} units")
print(f"{product_b_name}: {product_b_quantity} units")
print(f"{product_c_name}: {product_c_quantity} units")
print("\nSubtotal:", subtotal)
print("\nDiscount Applied: $", total_discount)
print("\nShipping Fee: $", shipping_fee)
print("\nGift Wrap Fee: $", total_gift_wrap_fee)
print("\nTotal: $", total_amount)