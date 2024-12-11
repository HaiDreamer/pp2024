#enter student in4 into a file, after that can extract in4 for listing function
"""Listing functions:
• List courses
• List students
• Show student marks for a given course"""

from datetime import datetime      #if import datetime only we have to change: dob = datetime.datetime.strptime(stu_dob, "%Y-%m-%d")
import json

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

#create a class student, class course, relationship: hasA (OOP)
class course:
    def __init__(self, id, mark):       #constructor
        self.id = id
        self.mark = mark

class student:
    def __init__(self, id, name, dob):  #constructor
        self.id = id
        self.name = name
        self.dob = dob
        self.courses = []
    def add_course(self, course):       #method
        self.courses.append(course)     #add multiply courses

students = []

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
        course_mark = float(input("Enter mark: "))
        cou = course(course_id, course_mark)
        stu.add_course(cou)

file_name = "students_data.json"

#save information into a file
with open(file_name, "w") as file:  #write mode
    data_to_save = [
        {
            "id": student.id,
            "name": student.name,
            "dob": student.dob.strftime("%Y-%m-%d"),    #convert date into string
            "course": [{"id": course_id, "mark": course_mark} for course in student.courses]    #error here !
        }
        for student in students
    ]
    json.dump(data_to_save, file, indent = 4)
print(f"Student data has been saved to {file_name}.")   
#return file-like object
#data_to_save: serializabe Py obj(dict, list, ..) into JSON format
#indent = 4: number of spaces used for indentation in the output JSON file

def list_courses():
    print("\nCourses:")
    courses = set()
    for student in students:
        for course in student.courses:
            courses.add(str(course.id)) #set value of course id as a string 
    print("\n".join(courses))

def list_students():
    for student in students:
        print(f"ID: {student.id}, Name: {student.name}, DOB: {student.dob}")

def show_student_marks(required_course_id):
    print(f"\nMark for course {required_course_id}:")
    for student in students:
        for course in student.courses:
            if course.id == required_course_id:
                print(f"Student {student.name} ({student.id}): {course.mark}")

#read information of a file
with open(file_name, "r") as file:  #open file "r" in read mode, choose file_name as a target
    loaded_data = json.load(file)   #load json file_name (file is file_name with read mode)
    students = []                   #initialize student list
    for student_data in loaded_data:        #loaded_data holds a list of dictionaries
        # Convert dob back to datetime object
        student_dob = datetime.strptime(student_data["dob"], "%Y-%m-%d")
        stu = student(student_data["id"], student_data["name"], student_data["dob"]) #init new student object
        for course_data in student_data["course"]:
            cou = course(course_data["id"], course_data["mark"])
            stu.add_course(cou)
        students.append(stu)    #new student assigned in a list "students"

# Menu for listing
while True:
    print("\nOptions:")
    print("1. List Courses")
    print("2. List Students")
    print("3. Show Student Marks for a Given Course")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        list_courses()
    elif choice == 2:
        list_students()
    elif choice == 3:
        course_id_input = str(input("Enter the course ID: "))
        show_student_marks(course_id_input)
    elif choice == 4:
        print("Exiting program.")
        break
    else:
        print("Invalid choice, please try again.")
