student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

def score_2_grade(dicti, dicti_gr):
    for i in dicti:
        if (dicti[i] > 90):
            dicti_gr[i] = "Outstanding"
        elif (dicti[i] > 80):
            dicti_gr[i] = "Exceeds Expectations"
        elif (dicti[i] > 70):
            dicti_gr[i] = "Acceptable"
        elif (dicti[i] < 70):
            dicti_gr[i] = "Fail"
    return dicti_gr

student_grades = {}
score_2_grade(student_scores, student_grades)