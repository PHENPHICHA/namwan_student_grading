#Assignment 2 Grading 10 Students using function and loop

def grading_function(std_name, std_score):
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

std_dict = {
            "Mark": 80, "Johny": 70, "Kevin": 60, "Jacob": 50, "Monica": 49,
            "Eric": 0, "Jackson": 81, "Winter": 69, "Jeno": 1, "Felix": 100
            }

for std_name, std_score in std_dict.items():
     grading_function(std_name, std_score)  
     
     