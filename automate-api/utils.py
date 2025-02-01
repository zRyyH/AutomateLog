import json

def load_json(path):
    with open(path, 'r', encoding='utf-8') as file:
        json_data = json.load(file)
        file.close()
    return json_data