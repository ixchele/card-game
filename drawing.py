import curses
import random

# rank (str): The rank of the card ('2'-'10', 'J', 'Q', 'K', 'A').
# suit (str): The suit of the card ('♠', '♥', '♦', '♣').
def creat_card(rank, suit):
    top = "┌─────────┐"
    bottom = "└─────────┘"
    side = "│         │"

    rank_left = f"{rank:<2}"
    rank_right = f"{rank:>2}"

    lines = [
        top,
        f"│{rank_left}       │",
        side,
        f"│    {suit}    │",
        side,
        f"│       {rank_right}│",
        bottom
    ]
    return "\n".join(lines)

def generate_deck():
    deck = []
    for suit in ('♠', '♥', '♦', '♣'):
        for rank in tuple(range(2,10)) + ('J', 'Q', 'K', 'A'):
            deck.append(creat_card(rank, suit))
    return deck

def shuffle_deck(deck):
    random.shuffle(deck)

def draw_card(deck):
    print(deck[0])
    return deck.pop(0)

def addstr_multiligne(win, y, x, texte):
    for i, ligne in enumerate(texte.split("\n")):
        win.addstr(y + i, x, ligne)

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
    title += "\t\t┳┓┓ ┏┓┏┓┓┏┓  ┏┳┏┓┏┓┓┏┓\n"
    title += "\t\t┣┫┃ ┣┫┃ ┃┫    ┃┣┫┃ ┃┫ \n"
    title += "\t\t┻┛┗┛┛┗┗┛┛┗┛  ┗┛┛┗┗┛┛┗┛\n"
    addstr_multiligne(stdscr, 0, 0, title)

def main(stdscr):
    deck = generate_deck()
    shuffle_deck(deck)
    curses.curs_set(0)
    while len(deck) != 0:
        print_header(stdscr)
        key = stdscr.getch()
        stdscr.clear()
        if key == ord('d'):
            addstr_multiligne(stdscr, 10, 0, draw_card(deck))
            addstr_multiligne(stdscr, 10, 7, draw_card(deck))
            stdscr.refresh()
        if key == ord('q'):
            break

curses.wrapper(main)

