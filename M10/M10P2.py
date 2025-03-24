def compsqf(length, width, height):
  sqf = (2 * length * width) + (2 * width * height)
  return sqf


answer = input("Do you want to calculate the square footage of the walls in the room? (y/n) ")
while answer == "y":
  length = float(input("Enter the length of the wall: "))
  width = float(input("Enter the width of the wall: "))
  height = float(input("Enter the height of the wall: "))
  sqf = compsqf(length, width, height)
  print(f"The square footage of the wall is: , {sqf: 0.2f}")
  gallons = sqf / 50
  print(f"The number of gallons of paint needed is: ", gallons)
  answer = input("Do you want to run this loop again? (y/n) ")
