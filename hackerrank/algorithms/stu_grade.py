
# https://www.hackerrank.com/challenges/grading
# 5 - 26 - 17


def solve(grades):
    new_grades = []
    for grade in grades:
        if (grade+1) % 5 == 0 and grade >= 38:
            new_grades.append((grade+1))
        elif (grade+2) % 5 == 0 and grade >= 38:
            new_grades.append((grade+2))
        else:
            new_grades.append(grade)

    return new_grades


n = int(input().strip())
grades = [int(input().strip()) for i in range(n)]

result = solve(grades)

print ("\n".join(map(str, result)))
