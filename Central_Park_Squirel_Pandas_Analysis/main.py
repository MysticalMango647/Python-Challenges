import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20260310.csv")

grey_squireels_count = len(data[data['Primary Fur Color'] == 'Gray'])
red_squireels_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squireels_count = len(data[data['Primary Fur Color'] == 'Black'])
print(grey_squireels_count)
print(red_squireels_count)
print(black_squireels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squireels_count, red_squireels_count, black_squireels_count]
}
print(data_dict)

df = pd.DataFrame(data_dict)
df.to_csv("squireel_count.csv")