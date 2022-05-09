num = [1, 2, 3]
new = [n + 1 for n in num]

test = [x * 2 for x in range(1, 5) if x > 3]

names = ["Alex", "Beth", "Caroline", "dave", "Eleanor", "freddie"]
short_names = [name.upper() for name in names if len(name) > 5]

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [x**2 for x in numbers]