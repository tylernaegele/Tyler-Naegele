answer = input("Do you want to start this loop ")
increment = 0 
totaldiscounts = 0
while answer.title().startswith("Y"):
  increment = increment + 1
  qty = int(input("What is the quantity? "))
  price = float(input("What is the price? "))
  extprice = qty * price
  if extprice > 10000:
    discount = extprice * 0.25
  else:
    discount = extprice * 0.10
  total = extprice - discount 
  totaldiscounts = totaldiscounts + discount
  print("The extended price is: $ ", extprice)
  print("The discount is: $ ", discount)
  print("The total is: $ ", total)
  answer = input("Do you want to run this loop again? ")
print("The sum of all the discounts is: $ ", totaldiscounts)