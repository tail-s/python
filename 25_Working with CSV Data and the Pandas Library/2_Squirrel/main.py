import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray = data[data["Primary Fur Color"] == "Gray"]
# gray = data[data["Primary Fur Color"] == "Gray"]
# gray = data[data["Primary Fur Color"] == "Gray"]