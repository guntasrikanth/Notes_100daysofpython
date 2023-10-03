with open("weather_data.csv") as file:
    data = file.readlines()
    print(data)


######## working with csv files using csv module ###############
# import csv
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperature = []
#     for row in data:
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))
#     print(temperature)

####### workign with csv files using pandas ################

import pandas

#data = pandas.read_csv("weather_data.csv")
# temp_list = data["temp"].to_list()
# count = 0
# avg = (sum(temp_list) // len(temp_list))
# print(avg)
# print(data['temp'].mean())
# print(data['temp'].max())

######## get data in columns
# print(data['condition'])   #accessing condition column as dict key pair values
# print(data.condition)  #accessing consition as an object of data variable

#### get data in row
# print(data[data['day'] == "Monday"])
# print(data[data['temp'] == data['temp'].max()])
# print(data[data.temp == data.temp.max()])

#### assigning a row data to a variable and accessing the row values by . method
# monday = data[data.day == 'Monday']
# monday_temp = monday.temp
# temp_f = monday_temp * 9/5 + 32
# print(temp_f)

#### Creating dataframe from scratch
data_dct = {
    "Student_name": ["Srija", "Lucky", "Harsha"],
    "Marks": [78, 75, 80]
}
new_data = pandas.DataFrame(data_dct)
new_data.to_csv("New_csv_file")
