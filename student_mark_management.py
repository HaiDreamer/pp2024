#enter student in4 into a file, after that can extract in4 for listing function

import datetime

num_student = int(input("Enter number of student(s): "))

#get date
def get_date():
    while True:
        stu_dob = input("Enter student dob(YYYY-MM-DD): ")
        try:
            dob = datetime.strptime(stu_dob, "%Y-%m-%d")
            return dob
        except ValueError:
            print("Invalid format, enter again.")

#just a demo
#create a class student, class course, relationship: hasA (OOP)
for i in range (num_student):
    student_id = str(input("Enter student ID: "))
    student_name = str(input("Enter student name: "))
    student_dob = get_date()
    num_course = int(input("Number of course(s): "))
    for j in range (num_course):
        course_id = str(input("Enter course_id: "))
        mark = float(int("Enter mark of this course: "))