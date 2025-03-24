def compnmf(month, sales):
  if month == "jan" or month == "feb" or month == "mar":
   f = 0.10
  elif month == "apr" or month == "may" or month == "jun":
     f = 0.15
  elif month == "jul" or month == "aug" or month == "sep":
     f = 0.20
  elif month == "oct" or month == "nov" or month == "dec":
     f = 0.25
  
  else:
    print("Invalid month entered")
    f= 0.00
  return (1.0 + f) * sales

answer= input("do you want to run this program? (yes/no)")
while answer == "yes":
  month = input("Enter the first 3 letters of a month: ")
  sales = float(input("Enter the sales for that month: "))
  nmf = compnmf(month, sales)
  print(f"The next month's forecast is  {nmf: .2f}")
  answer=str("do you want to run this program again? (yes/no)")
