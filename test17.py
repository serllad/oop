import curses
def main(stdscr):
    stdscr.clear()
    for i in range(11):
        v = i +1
        stdscr.addstr(i, 0, '10 divided by {} is {}'.format(v, 10 / v))
    stdscr.refresh()
    stdscr.getkey()

curses.wrapper(main)