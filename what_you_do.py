def who_are_you():

    name = input('Name:')
    return name


def what_you_do(name):
    positions = {
        'Nate Clark': 'Technical Director',
        'Sean Anthony': 'Director',
        'Kagan Coughlin': 'Co-Founder',
        'Glen Evans': 'Co-Founder',
        'Bethany Cooper': 'founding trustee',
        'Sage Nichols': 'founding trustee',
        'John Marsalis': 'founding trustee',
        'Carla Lewis': 'Trustee',
        'Martin Guzman': 'Graduated 2017',
        'Cole Anderson': 'Current Student',
        'Timothy Bowling': 'Current Student',
        'Logan Harrell': 'Current Student',
        'Desma Hervey': 'Current Student',
        'Ginger Keys': 'Current Student',
        'Matt Lipsey': 'Current Student',
        'Myeisha Madkins': 'Current Student',
        'Henry Moore': 'Current Student',
        'John Morgan': 'Current Student',
        'Irma Patton': 'Current Student',
        'Danny Peterson': 'Current Student',
        'Jakylan Standifer': 'Current Student',
        'Justice Taylor': 'Current Student',
        'Ray Turner': 'Current Student',
        'Cody van der Poel': 'Current Student',
        'Andrew Wheeler': 'Current Student'
    }
    if name in positions:
        job = positions[name]
        print(job)


def main():
    name = who_are_you()
    what_you_do(name)


if __name__ == '__main__':
    main()
