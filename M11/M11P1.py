def compdiscount(qty, price, rate):
    discamount = qty * price * rate
    discprice = qty * price - discamount
    return discprice, discamount

qty = int(input("Enter the quantity: "))
price = float(input("Enter the price: "))
rate = float(input("Enter the discount rate (in decimal form): "))

discamount, discprice = compdiscount(qty, price, rate)
print("Discounted price: ", discprice)
print("Discount amount: ", discamount)


