def grader():
    grades = []
    while True:
        grade = input('Grade:')
        if grade == 'grade':
            break
        elif grade.isdigit():
            grades.append(int(grade))

    average = sum(grades) / len(grades)
    if average >= 90:
        letter_grade = 'A'
    elif average >= 80:
        letter_grade = 'B'
    elif average >= 70:
        letter_grade = 'C'
    elif average >= 65:
        letter_grade = 'D'
    else:
        letter_grade = 'F'

    print('You averaged', average, 'and received a', letter_grade, '.')


def main():
    grader()


if __name__ == '__main__':
    main()
