def compcom(sales):
  if sales <= 100000:
    commission = sales * 0.05
    
  elif sales > 100000:
    commission = sales * 0.10
   
    target = sales * 0.05
    return commission, target

lastname = input("Enter the last name: ")
sales = float(input("Enter the sales: "))

commission, target = compcom(sales)

print("Last name: ", lastname)
print("Commission: ", commission)
print("Target: ", target)
