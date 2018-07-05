from random import shuffle


def ask_to_play_blackjack():
    while True:
        response = input('Are you game for a hand of Black Jack?')
        if response == 'Yes':
            print('Welcome to the Table!')
            choice = input('Would you like the instructions?')
            if choice == 'Yes':
                print(
                    'Players are each dealt two cards, face up or down depending on the casino and the table at which you sit. In the U.S., the dealer is also dealt two cards, normally one up (exposed) and one down hidden). In most other countries, the dealer receives one card face up. The value of cards two through ten is their pip value (2 through 10). Face cards (Jack, Queen, and King) are all worth ten. Aces can be worth one or eleven. A hand\'s value is the sum of the card values. Players are allowed to draw additional cards to improve their hands. A hand with an ace valued as 11 is called "soft", meaning that the hand will not bust by taking an additional card; the value of the ace will become one to prevent the hand from exceeding 21. Otherwise, the hand is "hard".Once all the players have completed their hands, it is the dealer’s turn. The dealer hand will not be completed if all players have either busted or received Blackjacks. The dealer then reveals the hidden card and must hit until the cards total 17 or more points. (At most tables the dealer also hits on a "soft" 17, i.e. a hand containing an ace and one or more other cards totaling six.) Players win by not busting and having a total higher than the dealer, or not busting and having the dealer bust, or getting a blackjack without the dealer getting a blackjack. If the player and dealer have the same total (not counting blackjacks), this is called a "push", and the player typically does not win or lose money on that hand. Otherwise, the dealer wins.'
                )
            elif choice == 'No':
                print('Ya feelin\' lucky, punk?')
            return 'Yes'

        elif response == 'Black':
            print('Jack')

        elif response == 'Black Jack':
            print('That is the game sir. Wanna Play?')

        elif response == 'No':
            print('Have a good day sir and you are welcome back any time!')
            break

        else:
            print('It is a yes or no question. Ya know that right?')


def blackjack():
    A = '11 or 1'
    K = 10
    Q = 10
    J = 10
    cards = [
        A, K, Q, J, 10, 9, 8, 7, 6, 5, 4, 3, 2, A, K, Q, J, 10, 9, 8, 7, 6, 5,
        4, 3, 2, A, K, Q, J, 10, 9, 8, 7, 6, 5, 4, 3, 2, A, K, Q, J, 10, 9, 8,
        7, 6, 5, 4, 3, 2
    ]
    for _ in range(5):
        shuffle(cards)
    response = ask_to_play_blackjack()
    if response == 'Yes':
        player_hand = cards[:2]
        print('Player\'s Hand:', player_hand)
        if A in player_hand:
            A = input('11 or 1?')
            if A == '11':
                A = 11
            elif A == '1':
                A = 1
            else:
                print('Please choose 11 or one.')
        dealer_hand = cards[2:4]
        print(dealer_hand)
        if A in dealer_hand:
            A = 11
        draw = input('Wanna take a hit?')
        if draw == 'Hit me':
            player_hand.append(cards.pop())
            if A in player_hand:
                A = input('11 or 1?')
                if A == '11':
                    A = 11
                elif A == '1':
                    A = 1
                else:
                    print('Please choose 11 or 1.')
            print(player_hand)
        else:
            print('Standing it is.')
        draw = input('Wanna take a hit?')
        if draw == 'Hit me':
            player_hand.append(cards.pop())
            if A in player_hand:
                A = input('11 or 1?')
                if A == '11':
                    A = 11
                elif A == '1':
                    A = 1
                else:
                    print('Please choose 11 or 1.')
            print(player_hand)
        elif draw == 'Stay':
            print('Standing it is.')
        else:
            print()

        if sum(dealer_hand) < 17:
            dealer_hand.append(cards.pop())
            if A in dealer_hand:
                A = 11

        if sum(player_hand) > 21:
            print('BUST! YOU LOSE!')
            print(player_hand, sum(player_hand))

        if sum(dealer_hand) > 21:
            print('DEALER BUST! YOU WIN!')
            print(dealer_hand, sum(dealer_hand))
        if sum(player_hand) <= 21 and sum(dealer_hand) < sum(player_hand):
            print('YOU WIN!!!')
            print(player_hand, sum(player_hand))


def main():
    blackjack()


if __name__ == '__main__':
    main()
