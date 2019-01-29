from random import shuffle
from collections import namedtuple
from time import sleep

ROYALTY = ['Jack', 'Queen', 'King']


def creating_deck(deck_size):
    """
    This function first creates a deck. Then shuffle it.
    """
    total_deck = []
    Card = namedtuple('Card', 'Value Suit')
    suits = ['Hearts', 'Diamonds', 'Club', 'Spade']
    values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']
    for _ in range(deck_size):
        for value in values:
            for suit in suits:
                total_deck.append(Card(value, suit))
    shuffle(total_deck)
    return total_deck


def card_pick(name, card_value, ace_checker, total_deck):
    """
    This function take 4 parameters which are name for user or dealer name,
    card_value for calculating value of given cards.
    ace_checker for if ace pulled from deck or not.
    total_deck is the our deck. This function calculates the value of current
    position and check if player is 21 or passed 21.
    """
    pick_card = total_deck.pop()
    if pick_card.Value in ROYALTY:
        card_value += 10
        print("{0} got {1} {2}. Total point {0} got: {3}"
              .format(name, pick_card.Suit, pick_card.Value, card_value))
    elif pick_card.Value == 'Ace':
        if card_value < 11:
            ace_checker = True
            card_value += 11
            print("{0} got {1} {2}. Total point {0} got: {3}"
                  .format(name, pick_card.Suit, pick_card.Value, card_value))
        else:
            card_value += 1
            print("{0} got {1} {2}. Total point {0} got: {3}"
                  .format(name, pick_card.Suit, pick_card.Value, card_value))
    else:
        card_value += pick_card.Value
        if ace_checker and card_value > 21:
            card_value -= 10
            print("{0} got {1} {2}. Total point {0} got: {3}"
                  .format(name, pick_card.Suit, pick_card.Value, card_value))
            ace_checker = False
        else:
            print("{0} got {1} {2}. Total point {0} got: {3}"
                  .format(name, pick_card.Suit, pick_card.Value, card_value))
    if card_value > 21 and name != "Dealer":
        print("İki zarda 80'lik olduk...")
        exit()
    elif card_value == 21 and name != "Dealer":
        print("Total value: {}. \n Blackjack, Kazandınız..".format(card_value))
        print_it()
        exit()
    return card_value, ace_checker


def pick_card_dealer(name, card_value, ace_checker, total_deck):
    """
    This function for closed card of the dealer in the beginning of the deal.
    """
    pick_card = total_deck.pop()
    unknown_card = pick_card
    if pick_card.Value in ROYALTY:
        card_value += 10
        print("{} got closed card".format(name))
    elif pick_card.Value == 'Ace':
        if card_value < 11:
            ace_checker = True
            card_value += 11
            print("{} got closed card".format(name))
        else:
            card_value += 1
            print("{} got closed card".format(name))
    else:
        card_value += pick_card.Value
        print("{} got closed card".format(name))
    return card_value, ace_checker, unknown_card


def print_it():
    """
    This function prints Freddie when player wins..
    """
    text = """
      '░█╚░         ░⌐
      ░╠░╛          ░⌐
      ░░╫═          ░⌐
      )░╙▓▄         ░░
      ║â▒▀▓▄        ░░
      ╣▒▒╣▓▓▄       ░░
      ╙▒▒╣╣▓▓▌      ░░
       ▒▒▒▒╣▀▓▄     ░░
       └▒▒▒▒▒▓▓∩    ░░
        ╟▒▌▒╣▓▓▓▄▄  ░░
         ▀▒▀╙░░░╚▀▀#░░
          ░   ⁿ  ⌐ ╚╚Q
         ]░   ╔╣╣╤  ░║▄
          ªg╤╣╬╢╬╣▒▒⌂╠▒▓
           ║╣╬╬╩░╩║╣▒╠▓▓▓▄      µ∞
         ▄█▀▒╔║▒▒╣╣╣╣╣║▓▓▓▓▄░Φ░░`
       @▀▀▓╫▄╬░▀╙░░░▒╣╣▓▓▓▓▓▓▓▄
      ▒▒╦╙▒▀░░░░░╣╣╬╬║╬▒▓▓▓▓▓▓▓▓⌐
    ▒▒╣▒╬║░░░░░]▌Q╦▄╣▓▓▓▓▓▀▀▀▓▓▓▌
    ,,▒▒▒╣▒▌░░╔▓▌▒▓▓▒▓▀▀▒▌▒▒▒▒▓▓▓▌
    ▒▒▒▒▒▓▓▓▓▓▓▌╗▓▓▓▌▌▒▒▒▒▌▒▒▒▒▒▒▓
      ▐▓▓▓▓▓▓╟▓╫▓▓▌╣▀▒▀▓▒▓▓▓▌▒▒▒▒▒
     Æ▒▒▒▒▒▒Θ▓▓▓╬▓▓▒▒╣░║▒▓▓▒▓▌▒▒╣▀
     ╙▀▀▒▒▒▌╟▓▓▓▓▒▒▒▒▒▒║╣▒▓▒▒▒▒▌▒∩
        ▀▀▀╜▀▀▀▀╜▀▀▀▀▀▀╜▀▀▀▀▀▀▀▀▀▀
    """
    print(text)


if __name__ == '__main__':
    u_name, d_name = "Player", "Dealer"
    check = False
    deck_count = int(input("How many decks will be in the game? --> "))
    deck = creating_deck(deck_count)
    user_value, ace_user = card_pick(u_name, 0, check, deck)
    int_value, ace_bank, closed_card = pick_card_dealer(d_name, 0, check, deck)
    user_value, ace_user = card_pick(u_name, user_value, ace_user, deck)
    bank_value, ace_bank = card_pick(d_name, 0, ace_bank, deck)
    while True:
        user_input = input('Do you wanna hit or stop?[h/s]')
        if user_input == 'h':
            user_value, ace_user = card_pick(u_name, user_value, ace_user, deck)
        elif user_input == 's':
            print("Evet beyler benim kumarım biter..")
            break
        else:
            print("Wrong input! Enter either h or s.")
    bank_value += int_value
    sleep(2)
    print(f'Dealer closed card is: {closed_card[1]} {closed_card[0]} '
          f'and total point of dealer is: {bank_value}')
    while True:
        sleep(2)
        if bank_value > 21:
            print("PLAYER WON")
            print_it()
            break
        elif bank_value == user_value and bank_value > 17:
            print("ITS DRAW")
            break
        elif bank_value > user_value:
            print("BANK WON")
            break
        bank_value, ace_bank = card_pick(d_name, bank_value, ace_bank, deck)
