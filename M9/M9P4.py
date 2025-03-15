def comppayrate(jobcode):
  if jobcode == "L":
    payrate = 25
  elif jobcode == "A":
    payrate = 30
  elif jobcode == "J":
    payrate = 50
  else:
    payrate = 0

  return payrate

def compgrosspay(hours, payrate):
  if hours > 40:
    grosspay = (hours * payrate * 1.5)
  else:
    grosspay = (hours * payrate)

  return grosspay

grosspaytotal = 0
answer = input("Do you want to calculate gross pay? (yes/no)")

while answer == "yes":
  lastname = input("Enter the last name: ")
  jobcode = input("Enter the job code (L, A, or J): ")
  hours = float(input("Enter the hours worked: "))
  payrate = comppayrate(jobcode)
  grosspay = compgrosspay(hours, payrate)
  grosspaytotal = grosspaytotal + grosspay
  print(lastname, "has a gross pay of $", grosspay)
  answer = input("Do you want to calculate gross pay? (yes/no)")

  print("The sum of all gross pay is $", grosspaytotal)