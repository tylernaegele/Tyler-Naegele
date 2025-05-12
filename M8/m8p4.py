# Create item data file
with open('item_data.txt', 'w') as file:
    file.write("Widget\n10\n50\n")
    file.write("Hammer\n2\n10\n")
    file.write("Saw\n4\n8\n")
    file.write("Drill\n1\n120\n")
    file.write("Wrench\n3\n15\n")

# Initialize accumulators
total_extended_price = 0
order_count = 0

# Read item data and calculate extended prices
with open('item_data.txt', 'r') as file:
    lines = file.readlines()

print("{:<10} {:>10} {:>10} {:>15}".format("Item", "Quantity", "Price", "Extended Price"))

for i in range(0, len(lines), 3):
    item = lines[i].strip()
    quantity = int(lines[i+1].strip())
    price = float(lines[i+2].strip())
    extended_price = quantity * price

    total_extended_price += extended_price
    order_count += 1

    print("{:<10} {:>10} ${:9,.2f} ${:14,.2f}".format(item, quantity, price, extended_price))

# Compute average order value
average_order = total_extended_price / order_count if order_count else 0

# Display summary
print("\nTotal value of orders: ${:,.2f}".format(total_extended_price))
print("Number of orders: {}".format(order_count))
print("Average order value: ${:,.2f}".format(average_order))
