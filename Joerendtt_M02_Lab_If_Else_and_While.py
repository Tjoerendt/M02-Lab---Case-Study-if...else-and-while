'''
Tyler Joerendt
Joerendtt_M02_Lab_if_Else_and_While.py
This program takes the students name and gpa and checks if the student qualified for honor roll or the dean's list
'''
lastName = "NA"
while lastName != "ZZZ":
    lastName = input("Input Student's Last Name: ")
    if lastName != "ZZZ":
        Gpa = float(input("Input Student's GPA: "))
        if Gpa >= 3.25:
            print(lastName + " has made the Honor Roll")
        if Gpa >= 3.5:
            print(lastName + " has made the Dean's List")