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

if __name__ == "__main__":
    deck = generate_deck()
    shuffle_deck(deck)
    while len(deck) != 0:
        draw_card(deck)









