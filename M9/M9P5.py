def comptuition(credits, dcode):
  if dcode == "i":
    tuition = credits * 250 
  elif dcode == "o":
    tuition = credits * 550

  return tuition

totaltuition = 0 
answer = input("Do you want to calculate the tuition? (yes/no): ")

while answer == "yes":
  credits = int(input("Enter the number of credits: "))
  dcode = input("Enter the district code (i/o): ")
  tuition = comptuition(credits, dcode)
  totaltuition = totaltuition + tuition
  print(f"The tuition for {credits} credits is ${tuition}")
  answer = input("Do you want to calculate the tuition? (yes/no): ")

print(f"The total tuition for all the students is $ {totaltuition}")
