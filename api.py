import requests
import json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

url = "http://brsapi.ir/FreeTsetmcBourseApi/Api_Free_Gold_Currency_v2.json"
request = requests.request("GET", url)
result_var = request.json()
var_interation = result_var["gold"]
with open ("taha.json", "w") as f:
    lst = []
    for i in var_interation:
        name = i.get("name")
        price = i.get("price")
        var_interation = {"name": name, "price":price}
        lst.append(var_interation)
    json.dump(lst, f)

class Data1(BaseModel):
    price: int

class Data2(BaseModel):
    name: str
    price: int

app = FastAPI()

with open("file1.json", "r") as f:
    database = json.load(f)

@app.get("/")
def getdata():
    return database

@app.post("/post/")
def postdata(data1: Data1):
    database.append(data1)
    return database

@app.put("/put/{put_name}")
def putdata(put_name: str, data2: Data2):
    for i, value in enumerate(db):
        if value["name"] == put_name:
            database[i] = data2.dict()
            return database
    raise HTTPException(status_code=404, detail="puterror")
