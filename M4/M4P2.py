# input phase
share_price = float(input("Enter the share price: "))
stock_price = float(input("Enter the stock price: "))
stock_qty = int(input("Enter the stock quantity: "))

# processing phase
value = (stock_price - share_price) * stock_qty

# output phase 
print(f"The value of the stock changed by ${value:.2f}")
