#Assignment 1 Grading 1 Student at a time using if else. 

std_name = "Penpicha"
std_score = 0

if std_score >= 80:
    print("Name: " + std_name + " Score: " + str(std_score) + " Grade = A")

elif std_score >= 70 and std_score < 80:
    print("Name: " + std_name + " Score: " + str(std_score) + " Grade = B")

elif std_score >= 60 and std_score < 70:
    print("Name: " + std_name + " Score: " + str(std_score) + " Grade = C")

elif std_score >= 50 and std_score < 60:
    print("Name: " + std_name + " Score: " + str(std_score) + " Grade = D")

else:
    print("Name: " + std_name + " Score: " + str(std_score) + " Grade = F")



