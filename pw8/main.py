from curses import wrapper 
import curses
from output import *
#from input import *         #to run enter student in4, delete '#'

# Menu for listing (use curse)
def main(stdscr):
    depress_file("studentLab6.dat")
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_GREEN)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_RED)
    blue_and_green = curses.color_pair(1)
    yellow_and_red = curses.color_pair(2)
    while True:
        stdscr.clear()      
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
        choice = stdscr.getch() - ord('0')     
    
        if choice == 1:
            stdscr.clear()
            stdscr.addstr(1, 0, list_courses()) 
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
            curses.echo()           
            course_id_input = stdscr.getstr(1, 0).decode()  
            curses.noecho()         
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
            compress_file_to_dat()
            break
        else:
            stdscr.clear()
            stdscr.addstr(1, 0, "Invalid choice, please try again.")
            stdscr.refresh()
            stdscr.getch()  

if __name__ == '__main__':
    wrapper(main)