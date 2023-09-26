import random
import time

loop_condition = True
deck = {
    "A": 11,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10
}
#   deck_cards = [key for key in deck.keys()]
#deck_poin
# ts = [value for value in deck.values()]

def deal_card():
    cards = [key for key in deck.keys()]
    my_card = random.choice(cards)
    return my_card
    # rand_index = random.randint(1,13)
    # my_card_index = [key for key in deck.keys()][rand_index-1]
    # return my_card_index

def evaluate_cards(cards):
    points = 0
    for card in cards:
        points += deck.get(card)
    if "A" in cards and points > 21:
            points -= 10
    return points

def is_blackjack(cards):
    if "J" in cards:
        if "Q" in cards or "K" in cards or "A" in cards or "10" in cards:
            return True
    return False

def start_game():    
    my_cards = [deal_card(),deal_card()]
    dealer_cards = [deal_card(),deal_card()]
    print(f"Dealer has {dealer_cards[0]}")
    print(f"My cards are: {my_cards[0], my_cards[1]}")
    if is_blackjack(my_cards):
        print("You won!")
        return
    if evaluate_cards(my_cards) == 21:
        print("You won!")
        return
    time.sleep(1)
    another_card = True
    while another_card:
        answer = input("Would you like another card? ")
        if answer == "y":
            my_cards.append(deal_card())
            print(my_cards)
            if is_blackjack(my_cards):
                print("You won!")
                return
            if evaluate_cards(my_cards) > 21:
                print("You lost!")
                return
        else:
            print("Your hand: ",my_cards)
            print("Dealer's hand:", dealer_cards)
            while evaluate_cards(dealer_cards) < 17:
                dealer_cards.append(deal_card())
            print("Your hand: ",my_cards)
            print("Dealer's hand:", dealer_cards)
            if evaluate_cards(dealer_cards) > 21:
                print("You won!")
                return
            elif evaluate_cards(my_cards) >= evaluate_cards(dealer_cards):
                print("You won!")
                return
            else:
                print("You lost")
                return


if __name__ == "__main__":
    while loop_condition:
        answer = input("Would you like to play BlackJack? ")
        if answer == "y":
            start_game()
        elif answer == "n":
            loop_condition = False
        else:
            print("Please answer by 'y' or 'n' ")
            continue
