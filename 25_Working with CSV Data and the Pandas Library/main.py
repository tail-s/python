# with open("./weather_data.csv") as w_data:
#     list = w_data.readlines()
#     print(list)

# import csv
#
# with open("weather_data.csv") as w_data:
#     data = csv.reader(w_data)
#     temp = []
#     for row in data:
#         t = row[1]
#         temp.append(t)
#     temp.pop(0)
#     print(temp)

import pandas

data = pandas.read_csv("weather_data.csv")

# # print(data["temp"])
# # print(type(data))
#
# data_dict = data.to_dict()
# # print(data_dict)
#
# temp_list = data["temp"].to_list()
# # print(temp_list)
#
# avg = sum(temp_list) / len(temp_list)
# print(avg)
#
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data.temp)

# print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])