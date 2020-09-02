from random import shuffle
from collections import namedtuple
from time import sleep

ROYALTY = ['Jack', 'Queen', 'King']


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit


def create_deck(deck_size):
    total_deck = []
    suits = ['Hearts', 'Diamonds', 'Club', 'Spade']
    values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']
    for _ in range(deck_size):
        for value in values:
            for suit in suits:
                total_deck.append(Card(value, suit))
    shuffle(total_deck)
    return total_deck


def print_card_deals(name: str, pick_card: object, card_value: int):
    print(f"{name} got {pick_card.suit} {pick_card.value}. "
          f"Total point {name} got: {card_value}")


def card_pick(name, hand_value, ace_checker, total_deck):
    pick_card = total_deck.pop()

    if pick_card.value in ROYALTY:
        hand_value += 10
        print_card_deals(name, pick_card, hand_value)
    elif pick_card.value == 'Ace':
        if hand_value < 11:
            ace_checker = True
            hand_value += 11
            print_card_deals(name, pick_card, hand_value)
        else:
            hand_value += 1
            print_card_deals(name, pick_card, hand_value)
    else:
        hand_value += pick_card.value
        if ace_checker and hand_value > 21:
            hand_value -= 10
            print_card_deals(name, pick_card, hand_value)
            ace_checker = False
        else:
            print_card_deals(name, pick_card, hand_value)

    hand_control(hand_value, name)

    return hand_value, ace_checker


def hand_control(hand_value, name):
    if hand_value > 21 and name != "Dealer":
        print("İki zarda 80'lik olduk...")
        exit()
    elif hand_value == 21 and name != "Dealer":
        print(f"Total value: {hand_value}. \n Blackjack, Kazandınız..")
        print_it()
        exit()


def pick_card_dealer(name, card_value, ace_checker, total_deck):
    """
    This function for closed card of the dealer in the beginning of the deal.
    """
    pick_card = total_deck.pop()
    unknown_card = pick_card
    if pick_card.value in ROYALTY:
        card_value += 10
        print(f"{name} got closed card")
    elif pick_card.value == 'Ace':
        ace_checker = True
        card_value += 11
        print(f"{name} got closed card")
    else:
        card_value += pick_card.value
        print(f"{name} got closed card")
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
    player, dealer, ace_check = "Player", "Dealer", False

    deck_count = int(input("How many decks will be in the game? --> "))
    deck = create_deck(deck_count)

    player_hand, player_ace = card_pick(player, 0, ace_check, deck)
    closed_card_value, dealer_ace, closed_card = pick_card_dealer(dealer, 0, ace_check, deck)
    player_hand, ace_user = card_pick(player, player_hand, player_ace, deck)
    dealer_hand, dealer_ace = card_pick(dealer, 0, dealer_ace, deck)

    while True:
        user_input = input('Do you wanna hit or stop?[h/s]')
        if user_input == 'h':
            player_hand, ace_user = card_pick(player, player_hand, ace_user, deck)
        elif user_input == 's':
            print("Evet beyler benim kumarım biter..")
            break
        else:
            print("Wrong input! Enter either h or s.")

    dealer_hand += closed_card_value
    sleep(2)
    print(f'Dealer closed card is: {closed_card.value} {closed_card.suit} '
          f'and total point of dealer is: {dealer_hand}')

    while True:
        sleep(2)
        if dealer_hand > 21 and dealer_ace:
            dealer_hand -= 10
            dealer_ace = False
        if dealer_hand > 21:
            print("PLAYER WON")
            print_it()
            break
        elif dealer_hand == player_hand and dealer_hand > 17:
            print("ITS DRAW")
            break
        elif dealer_hand > player_hand:
            print("BANK WON")
            break

        dealer_hand, dealer_ace = card_pick(dealer, dealer_hand, dealer_ace, deck)
