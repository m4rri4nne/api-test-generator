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

    for path, methods in paths.items():
        print(f"\nPath: {path}")
        for method, details in methods.items():
            print(f"  Method: {method.upper()}")
            parameters = details.get("parameters", [])
            if not parameters:
                print("    None parameter defined.")
            else:
                for param in parameters:
                    print(f"    Parameter: {param.get('name')} - In: {param.get('in')} - Required: {param.get('required')}")



def read_and_parse_swagger(file_location, swaggerType = "file"):
    if swaggerType == "file":
        swagger_data = read_swagger_file(file_location)
    elif swaggerType == "link":
        swagger_data = read_swagger_linked_file(file_location)
    else:
        print("❌ Invalid swagger type specified.")
        return

    parse_swagger(swagger_data)