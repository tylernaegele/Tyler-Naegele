students = { "Alice": 80, "Bob": 90, "Charlie": 75, "David": 85, "Eve": 95}

print(f"{'Student':>10} {'Grade':>10}")
print("-" * 21)

total = 0
for name, grade in students.items():
    print(f"{name:>10} {grade:>10}")
    total += grade

average = total / len(students)
print("-" * 21)
print(f"{'Average':>10} {average:>5.2f}")
