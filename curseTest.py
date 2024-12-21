# C:\Users\LT\Documents\GitHub\pp2024> python curseTest.py ->run program
# can't use normal way to run 
# UI = user interface
import curses
import time
from curses import wrapper

def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_GREEN)      #blue text, green wall
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_RED)      
    blue_and_green = curses.color_pair(1)
    yellow_and_red = curses.color_pair(2)

    pad = curses.newpad(100, 100)
    stdscr.refresh()

    for i in range(100):
        for j in range(28):
            char = chr(67 + j)
            pad.addstr(char, blue_and_green)

    #moving screen
    for i in range(50):     
        pad.refresh(0, i, 5, 5, 25, 75)
        time.sleep(0.2)
    stdscr.getch()

    # stdscr.addstr(10, 10, "Hello world", blue_and_green)  
    # stdscr.addstr(10, 10, "Hello world", curses.A_UNDERLINE)      #underline this text
    # stdscr.addstr(10, 12, "Hello world")                          #Overload previous line
    # stdscr.addstr(15, 20, "U are chicken", yellow_and_red | curses.A_BOLD)
    # print("Hello") can't use 
    '''counter_win = curses.newwin(1, 20, 10, 10)
    stdscr.addstr("hello me")
    stdscr.refresh()    # Calling stdscr.refresh() pushes the changes from the buffer to the actual terminal screen, making them visible.
    for i in range(100):
        stdscr.clear()
        color = yellow_and_red
        if i % 2 == 0:
            color = blue_and_green
        stdscr.addstr(f"Count: {i}", color)
        stdscr.refresh()
        time.sleep(0.1)
    stdscr.getch()
    #or
    for i in range(100):
        counter_win.clear() #clear the screen
        color = yellow_and_red
        if i % 2 == 0:
            color = blue_and_green
        counter_win.addstr(f"Count: {i}", color)
        counter_win.refresh()
        time.sleep(0.1)
    stdscr.getch()  #wait user press a key'''

wrapper(main)

