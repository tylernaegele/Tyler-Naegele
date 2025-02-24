lastname = input("Enter your last name: ")
salary = int(input("Enter your salary: "))
joblevel = int(input("Enter your job level: "))

if joblevel >= 10:\
  bonusrate = 0.25
elif joblevel >= 5:
  bonusrate = 0.2
else:
  bonusrate = 0.1

bonus = salary * bonusrate

print("Employee: ", lastname)
print("Bonus recieved: ", bonus)