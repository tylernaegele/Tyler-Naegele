students = { "Alice": [80, 90, 70], "Bob": [90, 95, 88], "Charlie": [75, 95, 70], "David": [85, 85, 90], "Eve": [95, 70, 95]}
def process_grades(student_dict):
  student_averages = []
  grade_totals = [0, 0, 0]
  num_students = len(student_dict)

  for name, grades in student_dict.items():
      avg = sum(grades) / len(grades)
      student_averages.append([name, avg])
      for i in range(3):
          grade_totals[i] += grades[i]

  class_averages = [total / num_students for total in grade_totals]
  return student_averages, class_averages

student_avgs, class_avgs = process_grades(students)
print(f"{'Student':<10} {'Average Grade':>15}")
print("-" * 26)

for name, avg in student_avgs:
    print(f"{name:<10} {avg:>15.2f}")

print("\nClass Averages for Each Grade:")
for i, avg in enumerate(class_avgs, start=1):
    print(f"Grade {i} Average: {avg:.2f}")