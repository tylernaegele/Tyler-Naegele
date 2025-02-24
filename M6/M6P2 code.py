partno = int(input("Enter part number: "))
qty = int(input("Enter quantity: "))

if partno == 10 or partno == 55:
    unitprice = 1.00
elif partno == 90:
    unitprice = 2.00
elif partno == 70 or partno == 80:
    unitprice = 3.00
else:
    unitprice = 5

total = float(qty) * unitprice

print("Part number: ", partno)
print("Unit price: ", unitprice)
print("Total: ", total) 