import pandas

# data = pandas.read_csv("weather_data.csv")
#
# # print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print(monday)
# monday_temp_fahrenheit = (int(monday.temp) * 1.8) + 32
# print(monday_temp_fahrenheit)

colors = ["Cinnamon", "Gray", "Black"]
squirrel_amount_list = []
color_dict = {"primary_color": colors, "amount_squirrels": squirrel_amount_list}
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
for color in colors:
    color_series = data[data["Primary Fur Color"] == color]
    squirrel_amount_list.append(len(color_series))

pandas.DataFrame.from_dict(color_dict).to_csv("final.txt")
