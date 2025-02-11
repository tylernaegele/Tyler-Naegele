# input phase
total = float(input( "Enter the total for the meal : "))

#proccessing phase 
tip_one = total * .15
tip_two = total * .18
tip_three = total * .20
tip_one_total = total + tip_one
tip_two_total = total + tip_two
tip_three_total = total + tip_three

# output phase 
print("With a %15 tip")
print( "Total: ", total)
print( "Tip: ", tip_one)
print( "Total with tip: ", tip_one_total)
print("           ")
print("With a %18 tip")
print( "Total: ", total)
print( "Tip: ", tip_two)
print( "Total with tip: ", tip_two_total)
print("           ")
print( "With a %20 tip")
print( "Total: ", total)
print( "Tip: ", tip_three)
print( "Total with tip: ", tip_three_total) 