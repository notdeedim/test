import random

def shuffle_card():
    value = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    suit = ["Hearts", "Spades", "Clubs", "Diamonds"]
    card_value = random.choice(value)
    card_suit = random.choice(suit)
    return card_value, card_suit
    
def interpreter():
    if card1[0] == 11:
        card1[0] = "Jack"
    elif card2[0] == 11:
        card2[0] = "Jack"
    elif card1[0] == 12:
        card1[0] = "Queen"
    elif card2[0] == 12:
        card2[0] = "Queen"
    elif card1[0] == 13:
        card1[0] = "King"
    elif card2[0] == 13:
        card2[0] = "King"
    elif card1[0] == 14:
        card1[0] = "Ace"
    elif card2[0] == 14:
        card2[0] = "Ace"
    else:
        pass
    return card1[0], card2[0]
    
card1 = list(shuffle_card())
card2 = list(shuffle_card())
    
print(card1, card2)

def comp():
    if card1[0] > card2[0]:
        interpreter()
        print(card1[0], "of", card1[1], "is bigger")
    else:
        interpreter()
        print(card2[0], "of", card2[1], "is bigger")
        
comp()
