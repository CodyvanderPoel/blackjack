from random import shuffle, randint

print(
    '____   _        ____     ____   __  __  ______      ____      ____  __  __'
)
print(
    '|  |  | |      / /\\\\     /___|  | | | | |_   _|    / /\\\\    /___| | | | |'
)
print(
    '|__/  | |     / /_\\ \\   | |     | |/ /    | |     / /_\\ \\  ||     | |/ /'
)
print(
    "|  \\  | |__  /_______\\  | |___  |   /   __| |    /_______\\ ||___  |   /"
)
print(
    '|__|  |___| /_/     \_\  \\___|  |_|\_\  \___/   /_/     \_\ \___| |_|\_\ '
)


def print_instructions():
    print('''
        Players are each dealt two cards, face up or down depending on the casino and the table at which you sit. 
        In the U.S., the dealer is also dealt two cards, normally one up (exposed) and one down hidden). 
        In most other countries, the dealer receives one card face up. 
        
        The value of cards two through ten is their pip value (2 through 10). 
        Face cards (Jack, Queen, and King) are all worth ten. 
        Aces can be worth one or eleven. A hand\'s value is the sum of the card values. 
        Players are allowed to draw additional cards to improve their hands. 
        
        A hand with an ace valued as 11 is called "soft", meaning that the hand will not bust 
        by taking an additional card; the value of the ace will become one to prevent the hand 
        from exceeding 21. Otherwise, the hand is "hard". 
        
        Once all the players have completed their hands, it is the dealer’s turn. 
        The dealer hand will not be completed if all players have either busted or received Blackjacks. 
        The dealer then reveals the hidden card and must hit until the cards total 17 or more points. 
        (At most tables the dealer also hits on a "soft" 17, i.e. a hand containing an ace and one or 
        more other cards totaling six.) Players win by not busting and having a total higher than the dealer, 
        or not busting and having the dealer bust, or getting a blackjack without the dealer getting a blackjack. 
        If the player and dealer have the same total (not counting blackjacks), this is called a "push", and the 
        player typically does not win or lose money on that hand. Otherwise, the dealer wins. If the dealer and the players 
        / player both start with a blackjack it is a tie.
        ''')


def ask_to_play_blackjack():
    while True:
        response = input('Are you game for a hand of Black Jack?').capitalize()
        if response == 'Yes':
            print('Welcome to the Table!')
            return response
        elif response == 'No':
            print('Have a good day sir and you are welcome back any time!')
            exit()
        else:
            print('It is a yes or no question. Ya know that right?')


def ask_for_instructions():
    while True:
        choice = input('Would you like the instructions?').capitalize().strip()
        if choice == 'Yes':
            print_instructions()
            break
        elif choice == 'No':
            print('Big shot, eh?')
            break


def make_deck():
    K = 10
    Q = 10
    J = 10
    return [
        'Ace', K, Q, J, 10, 9, 8, 7, 6, 5, 4, 3, 2, 'Ace', K, Q, J, 10, 9, 8,
        7, 6, 5, 4, 3, 2, 'Ace', K, Q, J, 10, 9, 8, 7, 6, 5, 4, 3, 2, 'Ace', K,
        Q, J, 10, 9, 8, 7, 6, 5, 4, 3, 2
    ]


def make_shoe():
    shoe = make_deck()
    for i in range(5):
        shoe.extend(make_deck())
    shuffle(shoe)
    return shoe


def hand_value(hand):
    '''List(cards) -> int
    
    >>> hand_value([4, 'Ace'])
    15
    '''
    hand_total = 0
    aces = 0
    for card in hand:
        if card == 'Ace':
            aces += 1
        else:
            hand_total = hand_total + card

    if aces == 0:
        return hand_total
    else:
        gap = 11 + (aces - 1)
        if hand_total + gap <= 21:
            return hand_total + gap
        else:
            return hand_total + aces


def players_turn(player_hand, shoe):
    while True:
        print('Player\'s Turn')
        draw = input('Wanna take a hit?').capitalize()
        if draw == 'Hit me':
            player_hand.append(shoe.pop())
            total = hand_value(player_hand)
            print(player_hand)
            if total > 21:
                print('BUST!!')
                break
            elif total == 21:
                print('BLACKJACK!!!')
                break
            continue
            print('Player\'s Hand:', player_hand)
        elif draw == 'Stay':
            break
        else:
            print('Hit me or Stay.')
        return player_hand


def dealers_turn(dealer_hand, shoe):
    while True:
        print('Dealer\'s Turn')
        if hand_value(dealer_hand) < 17:
            dealer_hand.append(shoe.pop())
            print('Dealer\'s hand:', dealer_hand[0], '?', dealer_hand[2:],
                  hand_value(dealer_hand))

        else:
            break


def winning_conditions(player_hand, dealer_hand):
    player, dealer = hand_value(player_hand), hand_value(dealer_hand)
    print('Player {}, total: {}'.format(player_hand, player))
    print('Dealer {}, total: {}'.format(dealer_hand, dealer))
    if player > 21:
        print('BUST! YOU LOSE!')
        print('DEALER WINS!')
        return 'lose'
    elif player == 21 and dealer != 21:
        print('BLACKJACK!!!')
        return 'blackjack'
    elif dealer > 21:
        print('DEALER BUST! YOU WIN!')
        return 'win'
    elif player == dealer:
        print('push')
        return 'push'
    elif player > dealer:
        print('YOU WIN!!!')
        return 'win'
    else:
        print('DEALER WINS!')
        return 'lose'


def betting(betting_money, winning_conditions):
    """
    Preconditions: bet must be greater than 0!
    """
    bet = input('How much are you willing to risk?')
    if bet.isdigit():
        if betting_money - int(bet) > 0:
            if winning_conditions == 'win':
                return (betting_money - int(bet)) + int(bet) * 2
            if winning_conditions == 'lose':
                return betting_money - int(bet)
            if winning_conditions == 'push':
                return betting_money
            if winning_conditions == 'blackjack':
                return (betting_money - int(bet)) + int(bet) * 2.5
        else:
            print('Not Enough Chips!')
    else:
        print('INVALID CHOICE!!')


def blackjack(betting_money):
    print('You have this much to gamble with:', betting_money)
    betting_money = betting(betting_money, winning_conditions)
    shoe = make_shoe()
    player_hand = [shoe.pop(), shoe.pop()]
    print('Player\'s Hand:', player_hand)
    hand_value(player_hand)
    dealer_hand = [shoe.pop(), shoe.pop()]
    print('Dealer\'s Hand:', dealer_hand[0], '?')
    players_turn(player_hand, shoe)
    dealers_turn(dealer_hand, shoe)
    winning_conditions(player_hand, dealer_hand)

    return betting_money


def game_play():
    betting_money = 100
    b = True
    while True:
        response = ask_to_play_blackjack()
        if response == 'Yes':
            if b:
                ask_for_instructions()
                b = False
        betting_money = blackjack(betting_money)


def main():
    game_play()


if __name__ == '__main__':
    main()
