# Create employee data file
with open('employee_data.txt', 'w') as file:
    file.write("Adams\n50000.00\n")
    file.write("Baker\n75000.00\n")
    file.write("Smith\n45000.00\n")
    file.write("Johnson\n120000.00\n")
    file.write("Brown\n35000.00\n")

# Initialize total bonus accumulator
total_bonus = 0

# Read employee data and calculate bonuses
with open('employee_data.txt', 'r') as file:
    lines = file.readlines()

print("{:<10} {:>10} {:>10}".format("Last Name", "Salary", "Bonus"))

for i in range(0, len(lines), 2):
    last_name = lines[i].strip()
    salary = float(lines[i+1].strip())

    if salary >= 100000:
        bonus_rate = 0.20
    elif salary >= 50000:
        bonus_rate = 0.15
    else:
        bonus_rate = 0.10

    bonus = salary * bonus_rate
    total_bonus += bonus

    print("{:<10} ${:9,.2f} ${:9,.2f}".format(last_name, salary, bonus))

# Display total bonuses
print("\nTotal bonuses paid out: ${:,.2f}".format(total_bonus))