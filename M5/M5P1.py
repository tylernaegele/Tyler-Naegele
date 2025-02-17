qty = int(input("Enter the quantity of an item: "))

if qty >= 1000:
  unit_price = 3.00
else:
  unit_price = 5.00

ext_price = qty * unit_price
tax = ext_price * 0.07
total = ext_price + tax

print("Quantity: ", qty)
print("Unit Price: ", unit_price)
print("Extended Price: ", ext_price)
print("Tax: ", tax)
print("Total: ", total)