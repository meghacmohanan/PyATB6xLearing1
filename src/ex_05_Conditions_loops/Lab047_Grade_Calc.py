
"""
Grade Calculator
A: 90-100
B: 80-89
C:70-79
D:60-69
F: 0-59
i/p- score= int
O/P- String
"""

score=int(input("Enter score: ").strip())
if 100 >= score >= 0:
    if 90 <= score <= 100:
        print("Grade is A")
    elif 80 <= score <= 89:
        print("Grade is B")
    elif 70 <= score <= 79:
        print("Grade is C")
    elif score >= 60 >= score:
        print("Grade is D")
    else:
        print("Grade is F")

else:
    print("Invalid score")









