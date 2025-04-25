class Student:
   
    tuition_rates = {
        'I': 250.00,  
        'O': 500.00,  
        'X': 800.00,  
        'G': 250.00
    }

    def __init__(self, first, last, district_code, credits):
        self.first = first
        self.last = last
        self.district_code = district_code.upper()
        self.credits = int(credits)

    def tuition_owed(self):
       
        rate = Student.tuition_rates.get(self.district_code, 500.00)
        return self.credits * rate


students = [
    Student('Emily', 'Chen', 'I', 12),  
    Student('Jake', 'Martinez', 'O', 15),  
    Student('Anya', 'Patel', 'X', 9), 
    Student('Liam', 'Nguyen', 'G', 6)
]


for s in students:
    print(f"{s.first} {s.last} (District {s.district_code}) owes: ${s.tuition_owed():.2f}")