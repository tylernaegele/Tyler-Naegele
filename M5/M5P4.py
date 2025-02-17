name = input("What is the name of the appliance? ")
cost = float(input("What is the cost of the appliance? "))

if cost > 1000:
  warranty = cost * 0.10
else:
  warranty = cost * 0.05

total = cost + warranty 


print ("The name of the appliance is: ", name)
print ("The cost of the appliance is: ", cost)
print ("The cost of the warranty is: ", warranty)
print ("The total cost is: ", total)