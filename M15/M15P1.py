
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print(f"Employee Name: {self.name}")
        print(f"Salary: ${self.salary:,.2f}")


class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def long_term_bonus(self):
        return self.salary * 0.40

    def display_info(self):
        super().display_info()
        print(f"Long-Term Bonus: ${self.long_term_bonus():,.2f}")


emp1 = Employee("Alice Johnson", 50000)
emp2 = Employee("Bob Smith", 60000)


mgr1 = Manager("Carol Williams", 90000)
mgr2 = Manager("David Lee", 110000)


print("== Employees ==")
emp1.display_info()
print()
emp2.display_info()
print("\n")


print("== Managers ==")
mgr1.display_info()
print()
mgr2.display_info()
