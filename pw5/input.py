from datetime import datetime      
import json
from domains.course import course
from domains.student import student

def get_date():
    while True:
        stu_dob = input("Enter student dob(YYYY-MM-DD): ")
        try:
            dob = datetime.strptime(stu_dob, "%Y-%m-%d")
            return dob
        except ValueError:
            print("Invalid format, enter again.")

students = []
num_student = int(input("Enter number of student(s): "))

for i in range (num_student):  
    print(f"Enter in4 for student #{i + 1}")
    student_id = str(input("Enter student ID: "))
    student_name = str(input("Enter student name: "))
    student_dob = get_date()
    stu = student(student_id, student_name, student_dob) 
    students.append(stu)
    num_course = int(input("Number of course(s): "))
    for j in range (num_course):
        course_id = str(input("Enter course_id: "))
        course_name = str(input("Enter name of course: "))
        course_mark = float(input("Enter mark: "))
        course_mark = round(course_mark, 1)
        cou = course(course_id, course_name, course_mark)
        stu.add_course(cou)

file_name = "lab4output.json"

with open(file_name, "w") as f: 
    data_to_save = [
        {
            "id": student.get_id(),
            "name": student.name,
            "dob": student.dob.strftime("%Y-%m-%d"),    #convert date into string
            "course": [{"id": course.get_id(), "name": course.name, "mark": course.get_mark()} for course in student.courses] 
        }
        for student in students
    ]
    json.dump(data_to_save, f, indent = 4)
    
print(f"Student data has been saved to {file_name}.")   