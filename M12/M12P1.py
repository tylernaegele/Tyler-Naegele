lastnames = ["John", "Doe", "Smith", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor"]

def names ():
  print ("Names in original order:")
  for lastname in lastnames: 
    print(lastname)

def names_reverse ():
  print ("Names in reverse order:")
  for lastname in reversed(lastnames):
    print(lastname)

names()
names_reverse()
