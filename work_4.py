import json
import datetime

data_dict={
    "updated":15,
    15:" ",
    "hello":"privet"
}

with open("data.json","w") as f:
    json.dump(data_dict,f)

with open("data.json","r") as f:
    data=json.load(f)

s=str(datetime.datetime.now())
for i in data:
    if i=="updated":
        data[i]=s
with open("data.json","w") as f:
    json.dump(data,f)
print(data)