def compbowling(score1, score2, score3, handicap):
   avg = (score1 + score2 + score3) / 3
   handicapavg = avg + handicap

   return handicapavg, avg

lastname = input("Enter your last name: ")
score1 = int(input("Enter your first score: "))
score2 = int(input("Enter your second score: "))
score3 = int(input("Enter your third score: "))
handicap = int(input("Enter your handicap (assume handicap percentage is at 100%): "))

handicapavg, avg = compbowling(score1, score2, score3, handicap)

print("Your last name is: ", lastname)
print(f"The average score is:  {avg:.0f}")
print(f"Your handicap average score is: {handicapavg: .0f}")
