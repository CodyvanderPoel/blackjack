from random import shuffle


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
        if card1 > card2:
            top.extend(cards[:])
            cards = []
            # print('Team1:', len(top), 'cards')
        elif card1 < card2:
            bottom.extend(cards[:])
            cards = []
            # print('Team2:', len(bottom), 'cards')
        # else:
        # print("DRAW")

        if len(top) == 0:
            shuffle(top_won)
            top.extend(top_won[:])
            top_won = []
        if len(bottom) == 0:
            shuffle(bottom_won)
            bottom.extend(bottom_won[:])
            bottom_won = []

        if count % 5000 == 0:
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
    for i in range(100000):
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
