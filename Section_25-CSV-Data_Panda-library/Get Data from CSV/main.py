import csv

import pandas

data = pandas.read_csv("weather_data.csv")

# Get data from a column
temp = data["temp"]
print(temp)