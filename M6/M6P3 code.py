principle = int(input("Enter the principle amount: "))
maturity = int(input("Enter the maturity amount: "))

if principle > 100000 and maturity == 5:
  int = 0.06
elif principle <= 100000 and principle >= 50000 and maturity == 10:
  int = 0.05
elif principle <= 100000 and principle >= 50000 and maturity == 5:
  int = 0.04
else:
  int = 0.02

yearone = principle * int

print("The principle value is: ", principle)
print("The interest rate is: ", int)
print("The interest amount for the first year is: ", yearone)
