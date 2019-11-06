
from csv import reader
import csv

opened_file = open("AppleStore.csv", encoding="utf-8")
read_file = reader(opened_file)

print(type(opened_file))

app_data = list(read_file)
# print(app_data[:5])
# print(len(app_data))
# print(app_data[0])
# print(app_data[1:3])