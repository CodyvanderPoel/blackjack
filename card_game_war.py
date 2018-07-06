from random import shuffle

#
#def i_declare_war(top, bottom):
#    top_card1 = top.pop()
#    top_card2 = top.pop()
#    top_card3 = top.pop()
#    top_card4 = top.pop()
#    bottom_card1 = bottom.pop()
#    bottom_card2 = bottom.pop()
#    bottom_card3 = bottom.pop()
#    bottom_card4 = bottom.pop()
#    if top_card4 > bottom_card4:
#        top_won.extend(cards)
#        cards = []
#    elif top_card4 > bottom_card4:
#        bottom_won.extend(cards)
#        cards = []
#    else:
#        top_card1 = top.pop()
#        top_card2 = top.pop()
#        top_card3 = top.pop()
#        top_card4 = top.pop()
#        bottom_card1 = bottom.pop()
#        bottom_card2 = bottom.pop()
#        bottom_card3 = bottom.pop()
#        bottom_card4 = bottom.pop()
#    if top_card4 > bottom_card4:
#        top_won.extend(cards)
#        cards = []
#    elif top_card4 > bottom_card4:
#        bottom_won.extend(cards)
#        cards = []


def war():
    A = 14
    K = 13
    Q = 12
    J = 11
    cards = [
        A, K, Q, J, 10, 9, 8, 7, 6, 5, 4, 3, 2, A, K, Q, J, 10, 9, 8, 7, 6, 5,
        4, 3, 2, A, K, Q, J, 10, 9, 8, 7, 6, 5, 4, 3, 2, A, K, Q, J, 10, 9, 8,
        7, 6, 5, 4, 3, 2
    ]
    # cards = [A, K, Q, J, 10, 9, 8, 7, 6, 5, 4, 3, 2][:] * 4
    for _ in range(10):
        shuffle(cards)
    top = cards[:26]
    bottom = cards[26:]
    # print(top)
    # print(bottom)
    cards = []
    count = 0
    top_won = []
    bottom_won = []
    while top and bottom:
        count += 1
        # print('Round', count)
        card1 = top.pop()
        card2 = bottom.pop()
        cards.extend([card1, card2])
        print(count, end=" ")
        if card1 > card2:
            top_won.extend(cards[:])
            cards = []
            print('You win:', len(top) + len(top_won), 'cards left')
        elif card1 < card2:
            bottom_won.extend(cards[:])
            cards = []
            print('You lose:', len(top) + len(top_won), 'cards left')
            # print('Team2:', len(bottom), 'cards')
        else:
            phrase = ['\nI', 'Declare', 'War!']
            for i in range(3):
                print(phrase[i], len(top) + len(top_won), 'cards left')
                if len(top) == 0:
                    shuffle(top_won)
                    top = top_won.copy()
                    top_won.clear()
                if len(bottom) == 0:
                    shuffle(bottom_won)
                    bottom = bottom_won.copy()
                    bottom_won.clear()

                if len(top) > 0 and len(bottom) > 0:
                    cards.append(top.pop())
                    cards.append(bottom.pop())
                else:
                    break

        if len(top) == 0:
            shuffle(top_won)
            top = top_won.copy())

        if count % 1000 == 0:
            top.extend(top_won[:])
            top_won = []
            bottom.extend(bottom_won[:])
            bottom_won = []
            shuffle(top)
            shuffle(bottom)
            top_won.clear()
        if len(bottom) == 0:
            shuffle(bottom_won)
            bottom = bottom_won.copy()
            bottom_won.clear()

        if count % 1000 == 0:
            top.extend(top_won[:])
            top_won = []
            bottom.extend(bottom_won[:])
            bottom_won = []
            shuffle(top)
            shuffle(bottom)

    if len(top) > len(bottom):
        return 'Player 1', count
        # print('Team 1 WINS!', len(top), 'cards')
        # print('Team 2 Loses!', len(bottom), 'cards')
    else:
        return 'Player 2', count
        # print('Team 2 WINS!', len(bottom), 'cards')
        # print('Team 1 Loses!', len(top), 'cards')


def main():
    games = {'Player 1': [], 'Player 2': []}
    for i in range(5):
        key, count = war()
        games[key].append(count)
        print(i)
    all_games = games['Player 1'][:] + games['Player 2'][:]
    print('max game', max(all_games))
    print('min game', min(all_games))
    print('average', sum(all_games) / len(all_games))
    print('player 1 win%:',
          round(100 * len(games['Player 1']) / len(all_games)), '%')


if __name__ == '__main__':
    main()
