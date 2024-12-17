import random


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def get_val_and_suit(self):
        return self.value, self.suit

    def get_val(self):
        return self.value


suits = ["club", "diamond", "heart", "spade"]
values = ["A", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
deck = []
wager = 100

for suit in suits:
    for value in values:
        card = Card(value, suit)
        deck.append(card)

random.shuffle(deck)


def get_card_info(hand):
    hand_info = []
    for card in hand:
        hand_info.append(card.get_val_and_suit())

    return hand_info


def get_hand_total_score(hand):
    total_score = 0
    for card in hand:
        card_val = card.get_val()
        if type(card_val) != str:
            total_score += card_val
        elif card_val == "A":
            total_score += 11
        else:
            total_score += 10
    return total_score


def play_game():
    dealers_full_hand = []
    users_full_hand = []

    deck_position = 0
    dealers_full_hand.append(deck[deck_position])
    deck_position += 1
    users_full_hand.append(deck[deck_position])
    deck_position += 1
    users_full_hand.append(deck[deck_position])
    deck_position += 1

    print(
        "Dealer has",
        str(get_card_info(dealers_full_hand)),
        "=",
        str(get_hand_total_score(dealers_full_hand)),
    )
    print(
        "You have",
        str(get_card_info(users_full_hand)),
        "=",
        str(get_hand_total_score(users_full_hand)),
    )

    if get_hand_total_score(users_full_hand) == 21:
        print("You won!")
    else:
        while True:
            user_move = str(input("What's your move? Hit (H), Stand (S): "))
            if user_move.lower() == "s":
                while True:
                    dealers_full_hand.append(deck[deck_position])
                    deck_position += 1
                    users_score = get_hand_total_score(users_full_hand)
                    dealers_score = get_hand_total_score(dealers_full_hand)
                    print(
                        "Dealer has",
                        str(get_card_info(dealers_full_hand)),
                        "=",
                        dealers_score,
                    )

                    if dealers_score > 21:
                        print("You won, dealer busted")
                        return True
                        break
                    if dealers_score == 17:
                        if dealers_score > users_score:
                            print("You lost, dealer won")
                            return False
                            break
                        elif dealers_score < users_score:
                            print("You won, dealer lost")
                            return True
                            break
                    if dealers_score > 17:
                        if dealers_score > users_score:
                            print("You lost, dealer won")
                            return False

                            break
                        if dealers_score < users_score:
                            print("You won, dealer lost")
                            return True
                            break
                    if dealers_score == users_score:
                        print("Tie, pushing")
                        break
                break
            elif user_move.lower() == "h":
                users_full_hand.append(deck[deck_position])
                deck_position += 1
                users_score = get_hand_total_score(users_full_hand)
                dealers_score = get_hand_total_score(dealers_full_hand)
                print(
                    "You have",
                    str(get_card_info(users_full_hand)),
                    "=",
                    users_score,
                )
                if users_score > 21:
                    print("You bust, dealer won")
                    return False
                    break
                elif users_score == 21:
                    print("You wont")
                    return True
            else:
                print("Please type S or H")


if __name__ == "__main__":
    print("Welcome to black jack!")
    print("Let the games begin")
    print("You start with $100")

    while wager > 0:
        bet = int(input(f"Enter wager amount (you have total ${wager}): "))
        if bet > wager:
            print(f"You dont have ${bet}")
            exit()
        won = play_game()
        if won == True:
            wager += bet
        elif won == False:
            wager -= bet
        else:  # if its a Tie it will return won = None
            pass
        random.shuffle(deck)
        print("\nNext round...\n")
    print("Oops you went bankrupt :(")
