student_marks = int(input("Enter the marks out of 100=  "))
if 0 <= student_marks <= 100:
    if student_marks in range(91, 101):
        print("Grade = A1")
    elif student_marks in range(81, 91):
        print("Grade = A2")
    elif student_marks in range(71, 81):
        print("Grade = B1")
    elif student_marks in range(61, 71):
        print("Grade = B2")
    elif student_marks in range(51, 61):
        print("Grade = c1")
    elif student_marks in range(40, 51):
        print("Grade = c2")
    else:
        print("Fail")
else:
    print("invalid marks")
