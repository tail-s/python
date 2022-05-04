import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray = data[data["Primary Fur Color"] == "Gray"]
cin = data[data["Primary Fur Color"] == "Cinnamon"]
black = data[data["Primary Fur Color"] == "Black"]

new_data = {
    "Fur Color": ["gray", "red", "black"],
    "Count": [len(gray), len(cin), len(black)]
}
ans = pandas.DataFrame(new_data)
ans.to_csv("squirrel_count.csv")