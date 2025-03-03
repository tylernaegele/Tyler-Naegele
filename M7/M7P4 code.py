answer = input("Do you want to start this loop ")
increment = 0 
grosspaytotal = 0
while answer.title().startswith("Y"):
  increment = increment + 1
  lastname = input("Enter your last name ")
  hours = float(input("Enter your hours worked "))
  rate = float(input("Enter the rate of pay "))
  if hours > 40:
    overtime = hours - 40
    overtime = overtime * rate * 1.5
    grosspay = (hours * rate) + overtime
  else:
    grosspay = hours * rate

  grosspaytotal = grosspaytotal + grosspay
  print("Last name: ", lastname)
  print("Gross pay: ", grosspay)
  
  answer = input("Do you want to run this loop again? ")
if increment > 0:
  avgpay = float(grosspaytotal / increment)
  print("Number of Employees: ", increment)
  print("Average pay: ", avgpay)