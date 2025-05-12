# Create student data file
with open('student_data.txt', 'w') as file:
    file.write("Jones\nI\n12\n")
    file.write("Adams\nI\n10\n")
    file.write("Baker\nO\n12\n")
    file.write("Smith\nO\n16\n")
    file.write("Clark\nI\n15\n")

# Initialize accumulators
total_tuition = 0
student_count = 0

# Read student data and calculate tuition
with open('student_data.txt', 'r') as file:
    lines = file.readlines()

print("{:<10} {:>10} {:>15}".format("Last Name", "Credits", "Tuition Owed"))

for i in range(0, len(lines), 3):
    last_name = lines[i].strip()
    district_code = lines[i+1].strip().upper()
    credits = int(lines[i+2].strip())

    cost_per_credit = 250.00 if district_code == 'I' else 500.00
    tuition = credits * cost_per_credit

    total_tuition += tuition
    student_count += 1

    print("{:<10} {:>10} ${:14,.2f}".format(last_name, credits, tuition))

# Display summary
print("\nTotal tuition owed: ${:,.2f}".format(total_tuition))
print("Number of students: {}".format(student_count))
