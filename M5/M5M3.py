books = int(input("Enter the number of books: "))
cost = float(input("Enter the cost per book: "))

order= books * cost

if order < 50:
  shipping = 0
else: 
  shipping = 25

total = order + shipping

print("Order total: $", total)
print("Shipping charge: $", shipping)