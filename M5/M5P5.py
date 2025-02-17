lastname = input("Enter your last name: ")
gross_income = float(input("Enter your gross income: "))
dependents = int(input("Enter the number of dependents: "))

adj_gross = gross_income - dependents * 12000

if adj_gross > 50000:
    tax = adj_gross * 0.20
else:
    tax = adj_gross * 0.10

if tax < 0:
    tax = 100

print("Last name: ", lastname)
print("gross_income: $ ", gross_income )
print("Number of dependents: ", dependents)
print("Adjusted gross income: $ " , adj_gross)
print("Income tax: $ " , tax)