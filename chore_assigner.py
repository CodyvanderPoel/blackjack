from random import shuffle


def chore_assigner():
    students = [
        'Cole', 'Timothy', 'Logan', 'Desma', 'Ginger', 'Matt', 'Myeisha',
        'Henry', 'John', 'Irma', 'Danny', 'Jakylan', 'Justice', 'Ray', 'Cody',
        'Andrew'
    ]
    chores = [
        'Monday Lunch', 'Tuesday Lunch', 'Wednesday Lunch', 'Thursday Lunch',
        'Friday Lunch', 'Friday Kitchen Clean', 'Friday Bathroom Small Clean ',
        'Friday Bathroom Large Clean', 'Daily Kitchen and Trash',
        'Daily Classroom and Trash', 'Wednesday Classroom Sweep',
        'Friday Classroom Sweep', 'Wednesday Hallway Sweep',
        'Friday Hallway Sweep', 'Friday Stairway Sweep',
        'Daily Inspections and Friday Wipe Down'
    ]
    shuffle(chores)
    for student in students:
        print(student, ':', chores.pop())


def main():
    chore_assigner()


if __name__ == '__main__':
    main()
