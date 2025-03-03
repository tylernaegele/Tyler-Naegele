answer = input("Do you want to start this loop ")
increment = 0 
grosspaytotal = 0
while answer.title().startswith("Y"):
  increment = increment + 1
  answer = input("Do you want to run this loop again? ")
print("done with" , increment, "loops")