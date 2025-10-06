import curses
import random
from typing import List
from Deck import Deck

# rank (str): The rank of the card ('2'-'10', 'J', 'Q', 'K', 'A').
# suit (str): The suit of the card ('♠', '♥', '♦', '♣').

def addstr_multiligne(win, y, x, texte):
    for i, ligne in enumerate(texte.split("\n")):
        win.addstr(y + i, x, ligne)


def center_text(win, texte):
    height, width = win.getmaxyx()
    lignes = texte.split("\n")
    start_y = (height - len(lignes)) // 2
    for i, ligne in enumerate(lignes):
        x = (width - len(ligne)) // 2
        win.addstr(start_y + i, x, ligne)

def print_header(stdscr):
    header = ""
    header += " /$$$$$$$  /$$        /$$$$$$   /$$$$$$  /$$   /$$          /$$$$$  /$$$$$$   /$$$$$$  /$$   /$$\n"
    header += "| $$__  $$| $$       /$$__  $$ /$$__  $$| $$  /$$/         |__  $$ /$$__  $$ /$$__  $$| $$  /$$/\n"
    header += "| $$  \\ $$| $$      | $$  \\ $$| $$  \\__/| $$ /$$/             | $$| $$  \\ $$| $$  \\__/| $$ /$$/ \n"
    header += "| $$$$$$$ | $$      | $$$$$$$$| $$      | $$$$$/              | $$| $$$$$$$$| $$      | $$$$$/  \n"
    header += "| $$__  $$| $$      | $$__  $$| $$      | $$  $$         /$$  | $$| $$__  $$| $$      | $$  $$  \n"
    header += "| $$  \\ $$| $$      | $$  | $$| $$    $$| $$\\  $$       | $$  | $$| $$  | $$| $$    $$| $$\\  $$ \n"
    header += "| $$$$$$$/| $$$$$$$$| $$  | $$|  $$$$$$/| $$ \\  $$      |  $$$$$$/| $$  | $$|  $$$$$$/| $$ \\  $$\n"
    header += "|_______/ |________/|__/  |__/ \\______/ |__/  \\__/       \\______/ |__/  |__/ \\______/ |__/  \\__/\n"
    title = ""
    title += "┳┓┓ ┏┓┏┓┓┏┓  ┏┳┏┓┏┓┓┏┓\n"
    title += "┣┫┃ ┣┫┃ ┃┫    ┃┣┫┃ ┃┫ \n"
    title += "┻┛┗┛┛┗┗┛┛┗┛  ┗┛┛┗┗┛┛┗┛\n"
    # addstr_multiligne(stdscr, 0, 0, title)
    center_text(stdscr, header)


def main(stdscr):
    curses.curs_set(0)

    while True:
        stdscr.border()
        print_header(stdscr)
        stdscr.refresh()

        key = stdscr.getch()
        stdscr.clear()

        if key == ord('q'):
            break
        elif key == ord('d'):
            if len(deck) >= 2:  # pour éviter erreur si deck < 2
                addstr_multiligne(stdscr, 10, 1, draw_card(deck))
                addstr_multiligne(stdscr, 10, 8, draw_card(deck))
                stdscr.refresh()
            elif len(deck) == 1:
                addstr_multiligne(stdscr, 10, 1, draw_card(deck))
            stdscr.refresh()
        if key == curses.KEY_RESIZE:
            stdscr.refresh()
            continue


curses.wrapper(main)

