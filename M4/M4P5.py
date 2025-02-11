# input phase
fixed_costs = float(input("Enter fixed costs: "))
unit_price = float(input("Enter the unit price: "))
unit_cost = float(input("Enter the unit cost: "))

# processing phase
break_even = fixed_costs / (unit_price - unit_cost) 

# output phase
print("Your Break even point is : ", break_even)
