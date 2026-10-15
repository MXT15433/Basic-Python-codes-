marks = float(input("Enter the marks obtained (0 to 100): "))

if marks < 0 or marks > 100:
    print("Invalid Input! Marks must be between 0 and 100.")
else:
    if marks >= 91:
        grade = "A1"
    elif marks >= 81:
        grade = "A2"
    elif marks >= 71:
        grade = "B1"
    elif marks >= 61:
        grade = "B2"
    elif marks >= 51:
        grade = "C1"
    elif marks >= 41:
        grade = "C2"
    elif marks >= 33:
        grade = "D"
    else:
        grade = "E"

    print("Your Grade is:",grade)

