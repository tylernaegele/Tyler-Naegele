# input phase
firstname = input( "Enter your first name: ")
steps = int(input( " Enter the number of steps you walked today: "))

# process phase
calories = steps * .25

# output phase
print(firstname + ", you burned " + str(calories))