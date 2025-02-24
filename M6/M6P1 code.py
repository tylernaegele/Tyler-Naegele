qty = int(input("Enter the quantity: "))

if qty > 10000:
    price = 10
elif qty >= 5000 and qty <= 10000:
    price = 20
else:
    price = 30

extprice = qty * price
tax = extprice * 0.07

print("Extended price: $", extprice)
print("Tax: $ {:.2f}" .format(tax))
print("Total: $", extprice + tax)

