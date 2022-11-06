def gradingStudents(grades):
    for i in range(len(grades)):
        if grades[i] >= 38:
            round = grades[i] // 5
            if ((5 * (round+1)) - grades[i]) < 3:
                grades[i] = 5 * (round+1)
            else:
                pass
        else:
            pass      
    return grades