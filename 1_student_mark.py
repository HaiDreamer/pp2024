from datetime import datetime 

file_name = "students_info.txt"

def get_date():
    while True:
        stu_dob = input("Enter student dob(YYYY-MM-DD): ")
        try:
            dob = datetime.strptime(stu_dob, "%Y-%m-%d")
            return dob
        except ValueError:
            print("Invalid format, enter again.")
        
students = int(input("Enter number of students: "))

with open(file_name, "w") as file:
    for i in range (students):
        print(f"Enter in4 for student #{i + 1}")
        student_id = str(input("Enter student ID: "))
        student_name = str(input("Enter student name: "))
        student_dob = get_date()
        file.write(f"Student ID: {student_id}, Name: {student_name}, DOB: {student_dob}\n")
        num_course = int(input("Number of course(s): "))
        for j in range (num_course):
            course_id = str(input("Enter course_id: "))
            course_mark = float(input("Enter mark: "))
            file.write(f"Course ID: {course_id}, Mark: {course_mark}\n")

#use dict here, extract information into a dict
file_name = "students_info.txt"

def parse_file(file_name):
    students = {}
    current_student = None

    with open(file_name, 'r') as file:
        for line in file:
            line = line.strip() #remove leading/trailing whitespace
            #check for student id line
            if line.startswith("Student ID"):
                parts = line.split(", ")    #Splits the string into a list of parts wherever there is a comma followed by a space (, ).
                student_id = parts[0].split(": ")[1]    #lay phan ben phai cua Student ID(index: 1)
                name = parts[1].split(": ")[1]
                dob = parts[2].split(": ")[1]
                #create new student entry
                current_student = student_id
                students[current_student] = {
                    "Name": name,
                    "DOB": dob,
                    "Courses": {}
                }
            elif line.startswith("Course ID"):
                parts = line.split(", ")
                course_id = parts[0].split(": ")[1]
                mark = float(parts[1].split(": ")[1])
                if current_student:         # Add course and mark to the current student
                    students[current_student]["Courses"][course_id] = mark
    return students

data = parse_file(file_name)
print(data)

def display_courses(data):
    print("\nCourses:")
    courses_ids = set()
    for std_id, std_info in data.items:
        courses = std_info.get('Courses', {})
        courses_ids.update(courses.keys())
    courses_ids = list(courses_ids)     #convert it into list
    print(courses_ids)

def display_students(data):
    print("\nStudents: ")
    students_names = set()
    for std_id, std_info in data.items:
        names = std_info.get('Name', {})
        students_names.update(names.keys())
    students_names = list(students_names)
    print(students_names)

display_courses(data)
display_students(data)