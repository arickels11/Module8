"""CIS 189
Alex Rickels
Topic 3 Assignment 1 - switch case"""

grade_dict = {
    'A': 90,
    'B': 80,
    'C': 70,
    'D': 60,
    'F': 59
}


def get_grade(grade):
    try:
        return grade_dict[grade]
    except KeyError:
        return 'none'


if __name__ == '__main__':
    print(get_grade('A'))
