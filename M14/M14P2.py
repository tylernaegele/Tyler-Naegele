class Student:
    def __init__(self, first, last, district_code, credits):
        self.first = first
        self.last = last
        self.district_code = district_code.upper()
        self.credits = int(credits)

    def tuition_owed(self):
        if self.district_code == 'I':
            rate = 250.00
        else:
            rate = 500.00
        return self.credits * rate


student1 = Student('Emily', 'Chen', 'I', 12)
student2 = Student('Jake', 'Martinez', 'O', 15)

print("Student 1:", student1.first, student1.last)
print("Tuition Owed: $", student1.tuition_owed())

print("Student 2:", student2.first, student2.last)
print("Tuition Owed: $", student2.tuition_owed())