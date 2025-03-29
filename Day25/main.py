# with open("./weather_data.csv", "r") as data:
#     weather_data = data.readlines()

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(row[1])
#     print(temperature)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])
#
# # Data dictionary
# data_dict = data.to_dict()
# print(data_dict)

# Temperature list
temp_list = data["temp"].to_list()
print(temp_list)

# Average temperature
average_temp = sum(temp_list) / len(temp_list)
print(average_temp)
print(data["temp"].mean())

# Maximum temperature
print()