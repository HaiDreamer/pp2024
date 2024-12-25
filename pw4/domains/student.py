from domains.attribute import att

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