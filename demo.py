def get_grade(marks,subject = "Unknown"):
    print("Subject:", subject)

    if marks < 0 or marks > 100:
        print("Invalid marks")
    elif marks >= 90:
        print("Grade: A")
    elif marks >= 80:
        print("Grade: B")
    elif marks >= 70:
        print("Grade: C")
    elif marks >= 60:
        print("Grade: D")
    else:
        print("Grade: F")        


get_grade(95, "Mathematics")
get_grade(85)