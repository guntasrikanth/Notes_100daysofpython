import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
colors = ['Gray', 'Cinnamon', 'Black']
count = []
for color in colors:
    data_list = len(data[data['Primary Fur Color'] == color])
    count.append(data_list)

new_dic = dict(Fur_Color=colors, count=count)
new_data = pandas.DataFrame(new_dic)
new_data.to_csv("Squirrel_count")