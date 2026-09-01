def grade_calculator():
    marks = int(input("Enter your marks: "))
    
    if 90 < marks <= 100:
        print("Grade: A")

    elif 80 <= marks < 90:
        print("Grade: B")

    elif 70 <= marks < 80:
        print("Grade: C")  

    elif 60 <= marks < 70:
        print("Grade: D")

    elif marks < 60:
        print("Grade: F")

    else:
        print("Invalid marks entered.")

grade_calculator()