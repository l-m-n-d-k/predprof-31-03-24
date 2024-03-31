import json
from flask import render_template, Flask, url_for, request
from markupsafe import escape

with open("data.json", "r", encoding="utf-8") as read_file:
    data = json.load(read_file)


app = Flask(__name__)



floor_count = data["rooms_count"]["data"]
windows_for_rooms = data["windows_for_room"]["data"]
s = sum(windows_for_rooms)
floors = data["windows"]["data"]
all_bools = []

for i in floors.values():
    all_bools.extend(i)

floors_123 = []
i = 0
for floor in floors:
    k = 0
    res = []
    for j in windows_for_rooms:
        res.append(all_bools[i * s + k: i * s + k+j])
        k += j
    floors_123.append({i: res})
    i += 1

rooms_count = 0
c = 0
rooms_nums = []
for elem in floors_123:
    for i, j in elem.items():
        for k in j:
            c += 1
            if True in k:
                rooms_count += 1
                rooms_nums.append(c)



@app.route('/')
@app.route('/index')
def hello(floor_count=floor_count, windows_for_rooms=windows_for_rooms):
    return render_template('index.html', 
                           floor_count=floor_count, 
                           windows_for_rooms=windows_for_rooms,
                           rooms_count=rooms_count,
                           rooms_nums=rooms_nums)


if __name__ == '__main__':
    app.run()