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

def GPA():  #student id, gpa
    stat = {}
    for student in students:
        total_score = 0
        total_course = 0
        for course in student.courses:
            total_score += course.get_mark()
            total_course += 1
        gpa = total_score / total_course
        stat.update({"student id:": student.get_id(), "gpa": gpa}) 
    sorted_stat = dict(sorted(stat.items(), key = lambda item: item[1]["gpa"]))
    print(sorted_stat)

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
    print("4. Show GPA")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        list_courses()
    elif choice == 2:
        list_students()
    elif choice == 3:
        course_id_input = str(input("Enter the course ID: "))
        show_student_marks(course_id_input)
    elif choice == 4:
        GPA()
    elif choice == 5:
        print("Exiting program.")
        break
    else:
        print("Invalid choice, please try again.")
