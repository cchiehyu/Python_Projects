# with open("weather_data.csv") as data:
#     data = data.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data:
#     data = csv.reader(data)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#         print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# # temperature = data['temp']
# # print(temperature)
# # # data_dict = data.to_dict()
# # # print(data_dict)
# #
# # # temp_list = data["temp"].to_list()
# # average_temp = data["temp"].mean()
# # max_temp = data["temp"].max()
# #
# # # Get data in columns
# # print(data.condition)
#
# # # Get data in rows
# # max_temp_row = data[data.temp == data.temp.max()]
# # monday = data[data.day == "Monday"]
# # #Convert Celsius to Fahrenheit T (℉) = T (℃) x 9/5 + 32
# # # Or, T (℉) = T (℃) x 1.8 + 32
# # monday_temp = int(monday.temp)
# # monday_temp_F = monday_temp * 9/5 + 32
# # print(monday_temp_F)

# Create a df from scratch

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

##Part 2 squirrel dataset

import pandas as pd
data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# Get data in columns
gray_squirrels = data[data["Primary Fur Color"] == "Gray"]
cinnamon_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]
black_squirrels = data[data["Primary Fur Color"] == "Black"]
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count =len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count =len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrels_count)
print(cinnamon_squirrels_count)
print(black_squirrels_count)

data_dict ={
    "Fur Color":["Gray","Cinnamon","Black"],
    "Count":[gray_squirrels_count,cinnamon_squirrels_count,black_squirrels_count]
}

df = pd.DataFrame(data_dict)
print(df)
df.to_csv("squirrels_count.csv")