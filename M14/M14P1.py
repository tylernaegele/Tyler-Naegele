
class Employee:
    def __init__(self, first, last, pay):
      self.first = first
      self.last = last 
      self.pay = pay 
      self.email = first + '.' + last + '@company.com'


    def bonus(self, rate):
      b = float(rate) * float(self.pay)
      return b

emp1 = Employee('Frank', 'Alvino',60000.00)

print(emp1.email)
print(emp1.first)
print(emp1.last)
print(emp1.pay)
print(emp1.bonus(0.10))
print(emp1.bonus(0.20))

