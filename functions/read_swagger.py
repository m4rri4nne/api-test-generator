import json
import requests

def read_swagger_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            swagger_data = json.load(file)
        return swagger_data
    except FileNotFoundError:
        print(f"❌ File not found: {file_path}")
    except json.JSONDecodeError:
        print(f"❌ Error when parsing the file: {file_path}")

def read_swagger_linked_file(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"❌ Error when calling the: {url}\nDetails: {e}")
    except json.JSONDecodeError:
        print(f"❌ Error when parsing the JSON received: {url}")

def parse_swagger(swagger_data):
    if not swagger_data:
        print("❌ None swagger data provided.")
        return
    paths = swagger_data.get("paths", {})
    if not paths:
        print("⚠️ None path was found in the swagger file.")
        return
    return paths

def read_and_parse_swagger(file_location, swagger_type = "file"):
    if swagger_type == "file":
        return read_swagger_file(file_location)
    elif swagger_type == "link":
        return read_swagger_linked_file(file_location)
    else:
        print("❌ Invalid swagger type specified.")
        return None


def get_path_info(path, swagger_data):
    for swagger_path, methods in swagger_data.get("paths", {}).items():
        if swagger_path == path:
            return methods
    print(f"❌ Path '{path}' not found in the swagger data.")
    return None