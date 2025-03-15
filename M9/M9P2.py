def compBA(hits, atbats):
  BA = hits / atbats
  return BA


totalplayers = 0
answer = input("Do you want to calculate a player's batting average? (yes/no) ")

while answer == "yes":
  name = input("Enter the player's name: ")
  hits = int(input("Enter the number of hits: "))
  atbats = int(input("Enter the number of at bats: "))
  BA = compBA(hits, atbats)
  print(f"name + 's batting average is  + {BA: .3f}")
  totalplayers = totalplayers + 1
  answer = input("Do you want to calculate another player's batting average? (yes/no) ")
print("You have calculated the batting average for " + str(totalplayers) + " players." )
