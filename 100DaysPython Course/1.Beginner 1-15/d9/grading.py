student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

for student in student_scores:
    score = int(student_scores[student])
    if (score < 60):
        print(student+": Meh")
    elif (score >= 60 and score <= 70):
        print(student+": Acceptable")
    elif(score > 70 and score <= 80):
        print(student+": LETS GOO")
    elif(score > 80 and score <= 90):
        print(student+": Acceptable")
    elif(score > 90 and score <= 100):
        print(student+": EXCELENT")
