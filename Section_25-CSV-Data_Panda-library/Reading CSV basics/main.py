# with open("weather_data.csv") as file:
#     data = file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# Read CSV file with Pandas
data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])

# Convert data to dictionary
# data_dict = data.to_dict()
# print(data_dict)

# Convert data to list
temperature_list = data["temp"].to_list()
# print(temperature_list)

# Getting average for temperature
# avg_temp = sum(temperature_list) / len(temperature_list)
avg_temp = data["temp"].mean()
# print(avg_temp)

# Getting max value for temperature
max_temp = data["temp"].max()
# print(max_temp)

# Get Data in Columns
# print(data["condition"])
# print(data.condition)

# Get Data in Rows
# print(data[data.day == "Monday"])

#   Get Row of data with MAX value
# print(data[data.temp == max_temp])
monday = data[data.day == "Monday"]
# print(monday.condition)

#   Convert to Fahrenheit
monday_fahrenheit = int((monday.temp * 1.8) + 32)
# print(monday_fahrenheit)

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

my_data = pandas.DataFrame(data_dict)
# Create a CSV file
data.to_csv("new_data.csv")

# Notes
# Pandas Library makes using data easier
