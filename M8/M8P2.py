# Initialize first two Fibonacci numbers
fib_sequence = [0, 1]

# Generate the first 20 Fibonacci numbers
for i in range(2, 20):
    next_number = fib_sequence[i-1] + fib_sequence[i-2]
    fib_sequence.append(next_number)

# Display the Fibonacci sequence
print("The first 20 numbers in the Fibonacci sequence are:")
for num in fib_sequence:
    print(num, end=" ")