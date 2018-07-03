from random import choice


def chore_assigner():
    students = [
        'Cole', 'Timothy', 'Logan', 'Desma', 'Ginger', 'Matt', 'Myeisha',
        'Henry', 'John', 'Irma', 'Danny', 'Jakylan', 'Justice', 'Ray', 'Cody',
        'Andrew'
    ]
    print(students)

    chores = [
        'Monday Lunch', 'Tuesday Lunch', 'Wednesday Lunch', 'Thursday Lunch',
        'Friday Lunch', 'Friday Kitchen Clean', 'Friday Bathroom Small Clean ',
        'Friday Bathroom Large Clean', 'Daily Kitchen and Trash',
        'Daily Classroom and Trash', 'Wednesday Classroom Sweep',
        'Friday Classroom Sweep', 'Wednesday Hallway Sweep',
        'Friday Hallway Sweep', 'Friday Stairway Sweep',
        'Daily Inspections and Friday Wipe Down'
    ]
    print(chores)

    while True:
        assigned_chore = []
        stdnt = []
        for student in students:
            stdnt.append(student)
        chr = []
        for chore in chores:
            chr.append(chore)
        assigned_chore.extend([stdnt.pop(), chr.pop()])
        print(assigned_chore)


def main():
    chore_assigner()


if __name__ == '__main__':
    main()
