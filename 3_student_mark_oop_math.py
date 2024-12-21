from datetime import datetime      # if import datetime only we have to change: dob = datetime.datetime.strptime(stu_dob, "%Y-%m-%d")
import json
import numpy as np
import curses
from curses import wrapper         # terminal-independent screen-painting and keyboard-handling facility 

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
    def __init__(self, id, name, mark):       
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
        if self.__courses:  #if has course, then run
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

for i in range (num_student):   #no need to fix 
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
    course_list = ""
    for course in courses:
        course_list += f"{course}\n"
    return course_list

def list_students():
    listStu = ""
    for student in students:
        listStu += f"ID: {student.get_id()}, Name: {student.name}, DOB: {student.dob}\n"
    return listStu

def show_student_marks(required_course_id):
    stMark = ""
    print(f"\nMark for course {required_course_id}:")
    for student in students:
        for course in student.courses:
            if course.get_id() == required_course_id:
                stMark += f"Student {student.name} ({student.get_id()}): {course.get_mark()}\n"
    return stMark

'''def GPA():  #student id, gpa
    stat = {}
    for student in students:
        total_score = 0
        total_course = 0
        for course in student.courses:
            total_score += course.get_mark()
            total_course += 1
        gpa = total_score / total_course
        stat[student.get_id()] = gpa        #add student gpa into dictionary
    sorted_stat = dict(sorted(stat.items(), key = lambda item: item[1]))    #at ascending order
    sorted_stat = dict(sorted(stat.items(), key = lambda item: item[1]), reverse = True) 
    #stats.items() return key-value pair
    #sorted()
    #   key=lambda item: item[1] -> sorted based on the second value(value) of each tuple(key, value)
    #   reverse = true: turn into descending order
    for student_id, gpa in sorted_stat.items():
        #print(f"{student_id}")              #print pair of key-value
        print(f"{student_id[0]}")            #print only key 
'''

#use numpy
def GPA():
    stat = {}
    for student in students:
       scores = [course.get_mark() for course in student.courses]
       score_arr = np.array(scores)
       gpa = np.mean(score_arr) if len(score_arr) > 0 else 0.0
       stat[student.get_id()] = gpa
    sorted_stat = dict(sorted(stat.items(), key = lambda item: item[1]), reverse = True)
    listGPA = ""
    for student_id, gpa in sorted_stat.items():
        listGPA += f"{student_id}: {gpa}\n"
    return listGPA

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

# Menu for listing (use curse)
def main(stdscr):
    #init color
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_GREEN)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_RED)
    blue_and_green = curses.color_pair(1)
    yellow_and_red = curses.color_pair(2)
    while True:
        stdscr.clear()      #clear terminal screen, apply pnly u call stdscr.refresh()
        stdscr.addstr(0, 0, "-----------------", blue_and_green)
        stdscr.addstr(1, 0, "Menu options", yellow_and_red)
        stdscr.addstr(2, 0, "1. List courses")
        stdscr.addstr(3, 0, "2. List students")
        stdscr.addstr(4, 0, "3. Show student marks for given course")
        stdscr.addstr(5, 0, "4. Show GPA")
        stdscr.addstr(6, 0, "5. Exit")
        stdscr.refresh()
        # User input
        stdscr.addstr(7, 0, "Enter your choice: ")
        stdscr.refresh()
        choice = stdscr.getch() - ord('0')      #convert keypress to int, is used to capture and process user input in a curses application.
    
        if choice == 1:
            stdscr.clear()
            stdscr.addstr(1, 0, list_courses()) #expect bytes or str
            stdscr.refresh()
            stdscr.getch()  
        elif choice == 2:
            stdscr.clear()
            stdscr.addstr(1, 0, list_students())
            stdscr.refresh()
            stdscr.getch()  
        elif choice == 3:
            stdscr.clear()
            stdscr.addstr(0, 0, "Enter the course ID: ")
            curses.echo()           # When a user types something, it will not be displayed in the terminal.
            course_id_input = stdscr.getstr(1, 0).decode()  # Get user input
            curses.noecho()         # When a user types something, it will appear on the terminal as they type.
            stdscr.clear()
            stdscr.addstr(1, 0, show_student_marks(course_id_input))
            stdscr.refresh()
            stdscr.getch()  
        elif choice == 4:
            stdscr.clear()
            stdscr.addstr(1, 0, GPA())
            stdscr.refresh()
            stdscr.getch()  
        elif choice == 5:
            stdscr.clear()
            stdscr.addstr(1, 0, "Exiting program.")
            stdscr.refresh()
            stdscr.getch()
            break
        else:
            stdscr.clear()
            stdscr.addstr(1, 0, "Invalid choice, please try again.")
            stdscr.refresh()
            stdscr.getch()  

wrapper(main)
