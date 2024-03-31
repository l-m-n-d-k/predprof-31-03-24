import json

with open('data.json', 'r', encoding='UTF-8') as file:
    data = json.load(file)

matrix = list()
for i in data['windows']['data']:
    string = [1 if j == True else 0 for j in data['windows']['data'][i]]
    for _ in string:
        string[string.index(_)] = (-1, _)
    matrix.append(string)
print(matrix)
