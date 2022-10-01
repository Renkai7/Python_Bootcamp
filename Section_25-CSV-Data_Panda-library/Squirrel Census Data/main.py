import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_color_count = len(data[data["Primary Fur Color"] == "Gray"])
red_color_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_color_count = len(data[data["Primary Fur Color"] == "Black"])

squirrel_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [gray_color_count, red_color_count, black_color_count]
}

my_data = pandas.DataFrame(squirrel_dict)
my_data.to_csv("squirrel_count.csv")
