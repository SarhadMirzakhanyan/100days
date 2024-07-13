# with open("./weather_data.csv") as f:
#     weather_lines = f.readlines()

# for line in weather_lines:
#     print(line.strip())


import pandas

# with open("./weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     tempretures = [int(line[1]) for line in data if data.line_num > 1]
#     print(tempretures)

squirall_data = pandas.read_csv(
    "./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"
    )
# print(data)
# list_temp = data["temp"].to_list()
# print(data["temp"].max())

black_squiral_count = (squirall_data["Primary Fur Color"] == "Black").sum()
red_squiral_count = (squirall_data["Primary Fur Color"] == "Cinnamon").sum()
gray_squiral_count = (squirall_data["Primary Fur Color"] == "Gray").sum()

df_dict = {
    "primary_color": ["Gray", "Red", "Black"],
    "Color_count": [gray_squiral_count, red_squiral_count, black_squiral_count]
}

squiral_df = pandas.DataFrame(df_dict)
squiral_df.to_csv("./squiral_count.csv")