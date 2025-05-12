# Get input from user
principal = float(input("Enter principle amount: "))
interest_rate = float(input("Enter interest rate: "))

# Initialize total interest accumulator
total_interest = 0

# Print formatted header
print("\n{:4} {:>15} {:>15}".format("Year", "Beginning", "Ending"))
print("{:>20} {:>15}".format("Balance", "Balance"))

# Loop through 5 years
for year in range(1, 6):
    beginning_balance = principal
    annual_interest = principal * interest_rate
    principal += annual_interest
    total_interest += annual_interest

    # Output formatted balances
    print("{:4} ${:14,.2f} ${:14,.2f}".format(year, beginning_balance, principal))

# Output total interest earned
print("\nTotal interest earned: ${:,.2f}".format(total_interest))
