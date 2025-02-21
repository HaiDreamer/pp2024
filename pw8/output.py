from datetime import datetime     
import json
import pickle
import zlib
import numpy as np
import threading

from domains.course import course
from domains.student import student

file_name = "lab6output.json"
students = []  

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

#using pickle
def compress_file_to_dat():
    def _compress():
        try:
            with open(file_name, "r") as jf:
                data = json.load(jf)
            serial_data = pickle.dumps(data)
            compress_data = zlib.compress(serial_data)
            with open("studentLab6.dat", "wb") as df:
                df.write(compress_data) 
        except Exception as e:
            print(f"[❌] Error: {e}") 
    thread = threading.Thread(target=_compress, daemon=True)
    #daemon=True makes this thread a daemon thread, meaning it will automatically exit when the main program ends.
    thread.start()  #starting the thread

def depress_file(dat_file):  
    try:
        with open(dat_file, "rb") as datFile:
            compressed_data = datFile.read()
        decompressed_data = zlib.decompress(compressed_data)
        json_data = pickle.loads(decompressed_data)                
        for student_data in json_data:        
            student_dob = datetime.strptime(student_data["dob"], "%Y-%m-%d")
            stu = student(student_data["id"], student_data["name"], student_dob) #init new student object
            for course_data in student_data["course"]:
                cou = course(course_data["id"], course_data["name"], course_data["mark"])
                stu.add_course(cou)
            students.append(stu) 
    except FileNotFoundError:
        print(f"Error: File '{dat_file}' not found.")
    except zlib.error as e:
        print(f"Error during decompression: {e}")
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

