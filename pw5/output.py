from datetime import datetime     
import json
import os
from pathlib import Path
import zlib
import numpy as np
import curses
from curses import wrapper

from domains.course import course
from domains.student import student

file_name = "lab5output.json"

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

#use numpy
def GPA():
    stat = {}
    for student in students:
       scores = [course.get_mark() for course in student.courses]
       score_arr = np.array(scores)
       gpa = np.mean(score_arr) if len(score_arr) > 0 else 0.0
       stat[student.get_id()] = gpa
    sorted_stat = dict(sorted(stat.items(), key = lambda item: item[1], reverse = True))
    listGPA = ""
    for student_id, gpa in sorted_stat.items():
        listGPA += f"{student_id}: {gpa}\n"
    return listGPA

#read information of a file
with open(file_name, "r") as file:
    loaded_data = json.load(file)           #error from here !
    students = []                   
    for student_data in loaded_data:        
        student_dob = datetime.strptime(student_data["dob"], "%Y-%m-%d")
        stu = student(student_data["id"], student_data["name"], student_data["dob"]) #init new student object
        for course_data in student_data["course"]:
            cou = course(course_data["id"], course_data["name"], course_data["mark"])
            stu.add_course(cou)
        students.append(stu)    

def depress_file_to_json(dat_file, json_file):
    try:
        with open(dat_file, "rb") as datFile:
            compressed_data = datFile.read()
        decompressed_data = zlib.decompress(compressed_data)
        decompressed_text = decompressed_data.decode("utf-8")   #decode into a string
        json_data = json.loads(decompressed_text)
        with open(json_file, "w") as jsonFile:
            json.dump(json_data, jsonFile, indent = 4)
    except FileNotFoundError:
        print(f"Error: File '{dat_file}' not found.")
    except zlib.error as e:
        print(f"Error during decompression: {e}")
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

#for testing without enter more input
'''def main(stdscr):
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

wrapper(main)'''