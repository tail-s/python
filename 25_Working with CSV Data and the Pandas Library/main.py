# with open("./weather_data.csv") as w_data:
#     list = w_data.readlines()
#     print(list)

import csv

with open("weather_data.csv") as w_data:
    data = csv.reader(w_data)
    temp = []
    for row in data:
        t = row[1]
        temp.append(t)
    temp.pop(0)
    print(temp)