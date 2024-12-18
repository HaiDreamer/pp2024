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
                parts = line.split(", ")
                student_id = parts[0].split(": ")[1]
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

data  = parse_file(file_name)
print(data)