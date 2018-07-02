from random import randint


def deaf_grandma():
    while True:
        response = input('You:')
        if response == 'BYE':
            print('Grandma: BYE SONNY')
            break
        elif response.isupper():
            print('Grandma:NO, NOT SINCE', randint(1930, 1950), '!')
        else:
            print('Grandma:HUH!? SPEAK UP SONNY!')


def main():
    deaf_grandma()


if __name__ == '__main__':
    main()
