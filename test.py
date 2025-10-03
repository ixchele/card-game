import curses

import curses

def main(stdscr):
    curses.curs_set(0)   # cacher le curseur
    stdscr.clear()

    # dessiner une bordure
    stdscr.border()

    stdscr.addstr(1, 2, "Fenêtre principale avec bordure")
    stdscr.refresh()

    stdscr.getch()

curses.wrapper(main)
