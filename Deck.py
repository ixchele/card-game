import random
from typing import List

class Deck:
    class Card:
        def __init__(self, rank: str, suit: str) -> None:
            self.rank = rank
            self.suit = suit
            self.card : str = self._creat_card() 

        def _creat_card(self) -> str:
            top = "┌─────────┐"
            bottom = "└─────────┘"
            side = "│         │"

            rank_left = f"{self.rank:<2}"
            rank_right = f"{self.rank:>2}"

            lines = [
                top,
                f"│{rank_left}       │",
                side,
                f"│    {self.suit}    │",
                side,
                f"│       {rank_right}│",
                bottom
            ]
            return "\n".join(lines)

        def __str__(self) -> str:
            return self.card

    def __init__(self) -> None:
        self.cards: List[Deck.Card] = self._generate_deck()
        
    def _generate_deck(self) -> List[Card]:
        deck: List[Deck.Card] = []
        for suit in ('♠', '♥', '♦', '♣'):
            for rank in tuple(str(i) for i in range(2,11)) + ('J', 'Q', 'K', 'A'):
                deck.append(self.Card(rank, suit))
        return deck

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw(self) -> "Deck.Card":
        return self.cards.pop(0)
