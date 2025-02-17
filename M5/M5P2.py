
item = input("Enter the name of the item: ")
qty = int(input("Enter the quantity of an item: "))

if item == "A":
   unit_price = 10
else:
   unit_price = 20
ext_price = qty * unit_price
print("The item is: ", item)
print("The unit price is: ", unit_price)
print("The extended price is: ", ext_price)
