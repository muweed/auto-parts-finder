
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/parts/search")
def search_parts(year: int, make: str, model: str, part_name: str):
    with open("mock_data.json", "r") as file:
        data = json.load(file)
    results = [item for item in data if item["make"] == make and item["model"] == model and part_name.lower() in item["part_name"].lower()]
    return {"results": results}
