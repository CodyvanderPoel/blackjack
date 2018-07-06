from random import shuffle


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
            choice = input('Would you like the instructions?').capitalize()
            if choice == 'Yes':
                print_instructions()
            elif choice == 'No':
                print('Big shot, eh?')
            return 'Yes'
        elif response == 'No':
            print('Have a good day sir and you are welcome back any time!')
            return 'No'

        else:
            print('It is a yes or no question. Ya know that right?')


def make_deck():
    A = 11
    K = 10
    Q = 10
    J = 10
    return [
        A, K, Q, J, 10, 9, 8, 7, 6, 5, 4, 3, 2, A, K, Q, J, 10, 9, 8, 7, 6, 5,
        4, 3, 2, A, K, Q, J, 10, 9, 8, 7, 6, 5, 4, 3, 2, A, K, Q, J, 10, 9, 8,
        7, 6, 5, 4, 3, 2
    ]


def make_shoe():
    shoe = make_deck()
    for i in range(5):
        shoe.extend(make_deck())
    shuffle(shoe)
    return shoe


def hand_value(hand):
    #A = '11 or 1'
    #aces = []
    #for card in hand:
    #    if card == A:
    #        hand.remove(A)
    #        aces.append(A)
    #    if sum(hand) > 10:
    #        A = 1
    #        hand.append(A)
    #    elif sum(hand) < 11:
    #        A = 11
    #        hand.append(A)

    return sum(hand)


def players_turn(player_hand, shoe):

    while True:
        print('Player\'s Turn')
        draw = input('Wanna take a hit?').capitalize()
        if draw == 'Hit me':
            player_hand.append(shoe.pop())
            hand_value(player_hand)
            print(player_hand)
        elif draw == 'Stay':
            break
        else:
            print('Hit me or Stay.')
        return player_hand


def dealers_turn(dealer_hand, shoe):
    while True:
        print('Dealer\'s Turn')
        if sum(dealer_hand) < 17:
            dealer_hand.append(shoe.pop())
        else:
            break


def winning_conditions(player_hand, dealer_hand):
    if sum(player_hand) == 21:
        print('BLACKJACK!!!')
    if sum(player_hand) > 21:
        print('BUST! YOU LOSE!')
        print('DEALER WINS!')
        print(player_hand, sum(player_hand))
    if sum(dealer_hand) > 21:
        print('DEALER BUST! YOU WIN!')
        print(dealer_hand, sum(dealer_hand))
    if sum(player_hand) <= 21 and sum(dealer_hand) < sum(player_hand):
        print('YOU WIN!!!')
        print(player_hand, sum(player_hand))
    if sum(dealer_hand) > sum(player_hand) and sum(dealer_hand) <= 21:
        print('DEALER WINS!')


def blackjack():
    shoe = make_shoe()
    while True:
        response = ask_to_play_blackjack()
        if response == 'No':
            break
        if response == 'Yes':
            player_hand = shoe[:2]
            print('Player\'s Hand:', player_hand)
            hand_value(player_hand)
            dealer_hand = shoe[2:4]
            print('Dealer\'s Hand:', dealer_hand)
            #if A in dealer_hand:
            #    A = 11
            players_turn(player_hand, shoe)
            dealers_turn(dealer_hand, shoe)
            winning_conditions(player_hand, dealer_hand)


def main():
    blackjack()


if __name__ == '__main__':
    main()
