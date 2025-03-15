def CompExtPrice(price, qty):
  extprice = price * qty

  if extprice > 10000:
    disc = extprice * 0.10
  else:
    disc = 0
  return extprice 


totalextprice = 0
response = input("Do you want to compute extended price? ")
while response == "yes":
  qty = float(input("Enter quantity: " ))
  price = float(input("Enter price: " ))
  extprice = CompExtPrice(price, qty)
  totalextprice = totalextprice + extprice
  print("Extended price: $", extprice)
  response = input("Do you want to compute exteded price? ")

print("Total extended price: $ ", totalextprice)

