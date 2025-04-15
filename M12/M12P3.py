def load_data():
    lastnames = []
    exam_scores = []
    with open("lastnames.txt", 'r') as file:
        for line in file:
            lastname, exam_score = line.strip().split('-')
            lastnames.append(lastname)
            exam_scores.append(int(exam_score))
        return lastnames, exam_scores


def display_all (lastnames, exam_scores):
    print ("Lastnames and Exam Scores:")
    for i in range(len(lastnames)):
        print(f"{lastnames[i]} - {exam_scores[i]}")


def display_highest(lastnames, exam_scores):
    high_var = 0
    high_index = 0
    for i in range(len(exam_scores)):
        if exam_scores[i] > high_var:
            high_var = exam_scores[i]
            high_index = i
    print (f"The highest score is {high_var}, scored by {lastnames[high_index]}") 

def display_lowest(lastnames, exam_scores):
  low_var = 999
  low_index = 0
  for i in range(len(exam_scores)):
      if exam_scores[i] < low_var:
          low_var = exam_scores[i]
          low_index = i
  print(f"The Lowest Score is {low_var}, scored by {lastnames[low_index]}")

lastnames, exam_scores = load_data()
display_all(lastnames, exam_scores)
display_highest(lastnames, exam_scores)
display_lowest(lastnames, exam_scores)