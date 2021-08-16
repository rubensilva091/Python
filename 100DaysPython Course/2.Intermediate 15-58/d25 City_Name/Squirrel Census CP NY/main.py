import pandas

FILE_CSV = "2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"

data = pandas.read_csv(FILE_CSV)
grey_squirrel = data[data["Primary Fur Color"] == "Gray"]
grey_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrel_count)
print(black_squirrel_count)
print(red_squirrel_count)



data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrel_count, red_squirrel_count, black_squirrel_count]
}


pandas.DataFrame(data_dict)
