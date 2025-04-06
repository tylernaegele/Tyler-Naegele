total = 0
tax = 0

def comptax(qty, price):
   global total, tax
   total = qty * price
   tax = total * 0.07
   return total, tax


qty = int(input("Enter quantity: "))
price = float(input("Enter price: "))

comptax(qty, price)
print(f"The total before tax is:  {total: .2f}")
print(f"The tax is:  {tax: .2f}")
