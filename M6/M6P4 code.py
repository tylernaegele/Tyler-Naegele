qty = int(input("Enter the quantity: "))

if qty >= 25:
    price = 50
elif qty >= 10:
    price = 60
elif qty >= 5:
    price = 70
else:
    price = 75

total = price * qty

print("Tickets bought: ", qty)
print("Price per ticket: ", price)
print("Total cost: ", total)
