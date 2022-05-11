num = [1, 2, 3]
new = [n + 1 for n in num]

test = [x * 2 for x in range(1, 5) if x > 3]

names = ["Alex", "Beth", "Caroline", "dave", "Eleanor", "freddie"]
short_names = [name.upper() for name in names if len(name) > 5]

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [x**2 for x in numbers]

# new_dict = {new_key:new_value for item in list}

# scores = [80, 90, 100, 95, 85, 75]
import random

students_scores = {student:random.randint(1, 100) for student in names}
passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}


