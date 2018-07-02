def grader():
    grades = []
    while True:
        grade = int(input('Grade:'))
        if grade >= 0:
            grades.append(grade)
        elif grade == 'grade':
            return grades
        else:
            print("please input a number or 'grade'")

    average = sum(grades) / len(grades)
    if average >= 90 and <= 100:
        letter_grade = 'A'
    elif average >= 80 and <= 89:
        letter_grade = 'B'
    elif average >= 70 and <= 79:
        letter_grade = 'C'
    elif average >= 65 and <= 69:
        letter_grade = 'D'
    else:
        letter_grade = 'F'
    
    print('You averaged',average,'and recieved a', letter_grade'.')


def main():
    grader()


if __name__ == '__main__':
    main()
