lastnames = ["John", "Doe", "Smith", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor"]
exam_scores = [88, 92, 78, 90, 85, 80, 95, 88, 75, 82]

def names_and_scores (lastnames, exam_scores):
  print ("Names and exam scores:")
  for i in range(len(lastnames)): 
    print(f"{lastnames[i]} - score: {exam_scores[i]}")

def names_reverse (lastnames, exam_scores):
  print ("Names Exam scores (Reversed):")
  for i in range(len(lastnames)-1, -1, -1):
   print (f"{lastnames[i]} - {exam_scores[i]}")
    

names_and_scores(lastnames, exam_scores)

names_reverse(lastnames, exam_scores)
