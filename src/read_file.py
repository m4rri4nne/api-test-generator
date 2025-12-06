import json

def read_swagger_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)
    return data
