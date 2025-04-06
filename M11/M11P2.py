def compaverage(exam1, exam2, exam3):
   avg = (exam1 + exam2 + exam3) / 3
   totalpoints = avg * 3
   return totalpoints, avg

lastname = input("Enter the student's last name: ")
exam1 = float(input("Enter the score for exam 1: "))
exam2 = float(input("Enter the score for exam 2: "))
exam3 = float(input("Enter the score for exam 3: "))
avg, totalpoints = compaverage(exam1, exam2, exam3)

print(f"The total points is: {avg:.2f}")
print(f"The total average is: {totalpoints: .2f}")
