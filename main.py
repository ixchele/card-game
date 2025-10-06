import curses
import random

if __name__ == "__main__":
    deck = generate_deck()
    shuffle_deck(deck)
    while len(deck) != 0:
        draw_card(deck)









