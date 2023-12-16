import json

DATA_FILE = 'data/airbnb.json'

def read_data():
    with open(DATA_FILE, 'r') as file:
        data = json.load(file)
    return data

def write_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=2)
