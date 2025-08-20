from fastapi import FastAPI
import json

app = FastAPI()
data = {}
@app.get("/")
def bal():
    return {"message": "Hello, World!"}

@app.get("/view")
def load_data():
    with open("patients.json", "r") as file:
        data = json.load(file)
    return data

@app.get("/patients/{id}")
def add_patient(id: str):
    data = load_data()
    for i in data:
        if i["id"] == id:
            return {"message": i}
