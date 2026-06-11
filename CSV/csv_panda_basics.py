import csv
#Using CSV
with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperature = []
    for row in data:
        if row[1] != "temp":
            temperature.append(row[1])
        #print(row)
    #print(temperature)

import pandas

data = pandas.read_csv("weather_data.csv")
#Outputs pandas dataframe
print(type(data))

#Outputs pandas series (basically a list)
print(type(data["temp"]))

#Convert to a dictionary
data_dict = data.to_dict()
print(data_dict)

#Convert to a list
temp_list = data['temp'].to_list()
print(temp_list)

#getting average of temp
print(data['temp'].mean())

#getting max temp
print(data['temp'].max())

#Pandas can also reference colom names without a list param, but rather a object
print(data.condition)

#Get data in row
print(data[data.day == "Monday"])

#Find which row in the df is equal to the max temp
print(data[data.temp == data.temp.max()])

#Get condition for monday
monday = data[data.day == "Monday"]
print(monday.condition)

#get temp and convert to Farenheit
monday_temp = monday.temp[0]
monday_temp_f = monday_temp *9/5+32
print(monday_temp_f)

#Create a data frame from scratch
data_dict = {
    "students": ["jonas", "chris", "annabelle"],
    "scores": [76,54, 97]
}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("student_data.csv")