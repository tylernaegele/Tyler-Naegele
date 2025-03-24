def compoutdoorprice(msrp, make, model, evc):
  if make == "Honda" and model == "accord":
    discount = 0.10
  elif make == "Toyota" and model == "Rav4":
    discount = 0.15
  elif evc == "y":
    discount = 0.30
  else:
    discount = 0.05
    
  return msrp + (msrp * 0.07) - (msrp * discount)
salestotal = 0
answer = input("Do you want to compute the price of a vehicle? (y/n): ")
while answer == "y":
  make = input("Enter the make of the vehicle: ")
  model = input("Enter the model of the vehicle: ")
  evc = input("Is the vehicle electric? (y/n): ")
  msrp = float(input("Enter the MSRP of the vehicle: "))
  outdoorprice = compoutdoorprice(msrp, make, model, evc)
  salestotal = salestotal + outdoorprice
  print("The out the door price of the vehicle is: $", outdoorprice)
  answer = input("Do you want to add another vehicle? (y/n): ")

print("The total sales price of all the vehicles is: $", salestotal)