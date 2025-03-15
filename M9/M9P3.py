def compmpg(miles, gallons):
  mpg = miles / gallons
  return mpg

trips = 0
answer = input("Do you want to calculate miles per gallon for your trip? (yes/no) ")

while answer == "yes":
  miles = float(input("Enter the number of miles driven: "))
  gallons = float(input("Enter the number of gallons used: "))
  mpg = compmpg(miles, gallons)
  print("Your miles per gallon for this trip is: ", mpg)
  trips = trips + 1
  answer = input("Do you want to add a trip? (yes/no) ")

print("You have calculated miles per gallon for ", trips, "trips.")
