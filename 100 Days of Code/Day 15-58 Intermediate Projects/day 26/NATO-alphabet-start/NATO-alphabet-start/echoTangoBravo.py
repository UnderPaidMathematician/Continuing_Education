import pandas as pd

# The hard way
natoDict = None
with open("nato_phonetic_alphabet.csv", 'r') as f:
    csvData = f.readlines()
    csvSplit = [x.replace("\n", '').split(",") for x in csvData[1:]]
    natoDict = {key: value for (key, value) in csvSplit}
    natoDict[" "] = " "

# User input
userInput = input("Enter a string:")
[print(natoDict[char]) for char in [x.upper() for x in userInput] if char in natoDict.keys()]


# Pandas Way
myData = pd.read_csv("nato_phonetic_alphabet.csv")
phoneticData = {value['letter']: value['code'] for (index, value) in myData.iterrows()}
phoneticData[' '] = ' '

[print(phoneticData[char]) for char in [x.upper() for x in userInput] if char in phoneticData.keys()]


test = [x for x in myData.iterrows()]
print("pause")

