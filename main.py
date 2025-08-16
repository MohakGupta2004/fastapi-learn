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


