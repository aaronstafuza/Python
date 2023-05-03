# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     for row in data:
#         print(row[1])

import pandas
data = pandas.read_csv("weather_data.csv")
# print(data["temp"]) 

# data_dict = data.to_dict()
# print(data_dict)

temp_12 = data[data["temp"] == 12]
temp_12_len = len(data[data["temp"] == 12])
print(temp_12)
print(temp_12_len)