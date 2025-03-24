def compassessedvalue(county, markertvalue):
  if county == "cook":
    avp = 0.90
  elif county == "dupage":
    avp = 0.80 
  elif county == "mchenry":
    avp = 0.75
  elif county == "kane":
    avp = 0.60 
  else:
    avp = 0.70

  assessedvalue = marketvalue * avp
  return assessedvalue
markettotal = 0
assessedtotal = 0
answer = input("Do you want to run the program? (y/n)")
while answer == "y":
  county = input("Enter the county: ")
  marketvalue = float(input("Enter the market value: "))
  assessedvalue = compassessedvalue(county, marketvalue)
  markettotal = markettotal + marketvalue
  assessedtotal = assessedtotal + assessedvalue
  print("Assessed value: $", assessedvalue)
  answer = input("Do you want to add another property? (y/n)")

print("Total market value: $", markettotal)
print("Total assessed value: $", assessedtotal)

