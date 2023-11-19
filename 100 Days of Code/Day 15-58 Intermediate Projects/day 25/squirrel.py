import pandas as pd

squirrelData = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

furColorTypes = squirrelData["Primary Fur Color"].dropna().unique()

furColorData = pd.DataFrame(columns=["Fur Color", "Count"])
print("pause")
squirrelTypeAndColorList = []
for color in furColorTypes:
    squirrelTypeAndColorList.append([color, squirrelData["Primary Fur Color"][squirrelData["Primary Fur Color"] == color].count()])

tempDataFrame = pd.DataFrame(squirrelTypeAndColorList, columns=furColorData.columns)

furColorData = pd.concat([furColorData, tempDataFrame], ignore_index=True)

furColorData.to_csv("mySquirrelCount.csv")
print("pause")