# Task 3: Conditional Statements & Logical Flow
# Grade Calculation Program

# Get marks from user
marks = int(input("Enter your marks (0 - 100): "))

# Validate marks range
if marks < 0 or marks > 100:
    print("Invalid marks! Please enter a value between 0 and 100.")

else:
    # Determine grade based on marks
    if marks >= 90:
        grade = "A"
        result = "Pass"
    elif marks >= 75:
        grade = "B"
        result = "Pass"
    elif marks >= 60:
        grade = "C"
        result = "Pass"
    elif marks >= 40:
        grade = "D"
        result = "Pass"
    else:
        grade = "F"
        result = "Fail"

    # Display result
    print("Marks:", marks)
    print("Grade:", grade)
    print("Result:", result)
