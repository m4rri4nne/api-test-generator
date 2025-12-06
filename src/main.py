import json
import read_file

def main():
    swagger_data = read_file.read_swagger_file("swaggerexample.json")
    for path, methods in swagger_data.get("paths", {}).items():
        print (f"Path: {path}")
        for method, details in methods.items():
            print (f"  Method: {method.upper()}")
            parameters = details.get("parameters", [])
            for param in parameters:
                print (f"    Parameter: {param.get('name')} - In: {param.get('in')} - Required: {param.get('required')}")

if __name__ == "__main__":
    main()
