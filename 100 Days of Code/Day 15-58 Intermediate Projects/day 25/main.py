import pandas as pd
import csv

myData = pd.read_csv(r"C:\PythonProjects\100daysofcode\day 25\weather_data.csv")
monday = myData[myData['day'] == 'Monday']
print(monday)
print(monday['temp']*(9/5)+32)

dataDict = {"students": ["Amy", "Jamos", "Angela"], "scores": [76, 56, 65]}

studentData = pd.DataFrame(dataDict)
print(studentData)
studentData.to_csv(path_or_buf=r"studentData.csv")