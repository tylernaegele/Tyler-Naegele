def compprice(miles):
  if miles >= 30:
    ticketprice = 12
  elif miles >= 20:
    ticketprice = 10
  elif miles >= 10:
    ticketprice = 8
  else:
    ticketprice = 5

  return ticketprice
sumtickets = 0 
answer = input("Would you like to run the program? (y/n) ")
while answer == "y":
  lastname = input("Enter your last name: ")
  miles = float(input("Enter the number of miles from downtown Chicago: "))
  ticketprice = compprice(miles)
  sumtickets = sumtickets + ticketprice
  print("The ticket price is $", ticketprice)
  answer = input("Would you like to run the program again? (y/n) ")
print("The sum of all ticket prices is $", sumtickets)
