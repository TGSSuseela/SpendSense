# data_store.py
import json
import os

DATA_FILE = "user_data.json"

def _load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def _save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def update_user(user_id: str, key: str, value):
    data = _load_data()
    if user_id not in data:
        data[user_id] = {}
    data[user_id][key] = value
    _save_data(data)
