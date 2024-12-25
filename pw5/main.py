from curses import wrapper 
import curses
from output import *
from input import *

# Menu for listing (use curse)
def main(stdscr):
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