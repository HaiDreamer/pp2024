from datetime import datetime      #if import datetime only we have to change: dob = datetime.datetime.strptime(stu_dob, "%Y-%m-%d")
import json

def get_date():
    while True:
        stu_dob = input("Enter student dob(YYYY-MM-DD): ")
        try:
            dob = datetime.strptime(stu_dob, "%Y-%m-%d")
            return dob
        except ValueError:
            print("Invalid format, enter again.")

class att:
    def __init__(self, id, name):
        self.__id = id
        self.name = name
    def set_id(self, id):
        self.__id = id
    def get_id(self):
        return self.__id
    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name
        
class course(att):
    def __init__(self, id, name, mark):       #constructor
        super().__init__(id, name)
        self.__mark = mark
    def set_mark(self, mark):
        self.__mark = mark
    def get_mark(self):
        return self.__mark

class student(att):
    def __init__(self, id, name, dob): 
        super().__init__(id, name)
        self.dob = dob
        self.__courses = []
    def add_course(self, course):     #add single course
        self.__courses.append(course)  
    def show_course(self):
        if self.__courses:
            print(f"Course for {self.name}:")
            for index, course in enumerate(self.__courses, start = 0):  #iterate over the sequence, default: start = 0
                print(f"{index}. {course}")
        else:
            print(f"No courses assigned to {self.name}.")
    @property       #allow to retreive __courses attribute while keeping in private
    def courses(self):
        """Getter for courses."""
        return self.__courses
    @courses.setter
    def courses(self, course_list):
        if isinstance(course_list, list) and all(isinstance(course, str) and course.strip() for course in course_list):
            self.__courses = course_list
        else:
            raise ValueError("Courses must be a list or string")

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
        cou = course(course_id, course_name, course_mark)
        stu.add_course(cou)

file_name = "lab3output.json"

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

def list_courses():
    print("\nCourses:")
    courses = set()
    for student in students:
        for course in student.courses:
            courses.add(str(course.get_id())) #set value of course id as a string 
    print("\n".join(courses))

def list_students():
    for student in students:
        print(f"ID: {student.get_id()}, Name: {student.name}, DOB: {student.dob}")

def show_student_marks(required_course_id):
    print(f"\nMark for course {required_course_id}:")
    for student in students:
        for course in student.courses:
            if course.get_id() == required_course_id:
                print(f"Student {student.name} ({student.get_id()}): {course.get_mark()}")

#read information of a file
with open(file_name, "r") as file:
    loaded_data = json.load(file)   #load json file_name (file is file_name with read mode)
    students = []                   
    for student_data in loaded_data:        #loaded_data holds a list of dictionaries
        # Convert dob back to datetime object
        student_dob = datetime.strptime(student_data["dob"], "%Y-%m-%d")
        stu = student(student_data["id"], student_data["name"], student_data["dob"]) #init new student object
        for course_data in student_data["course"]:
            cou = course(course_data["id"], course_data["name"], course_data["mark"])
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
