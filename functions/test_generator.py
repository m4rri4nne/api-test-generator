from google import genai
from dotenv import load_dotenv
import os
from assets import theme


def test_generator(path, method, swagger_data):
    print(f"Generating tests for {method.upper()} {path}...")
    details = swagger_data["paths"][path][method]
    request_body = ""
    parameters = ""
    # Getting information about the endpoint
    if 'tags' not in details:
        endpoint_name = path
    elif len(details['tags']) == 0:
        endpoint_name = path
    else:
        endpoint_name = details['tags'][0]
    if 'requestBody' in details:
        request_body = details['requestBody']
    if 'parameters' in details:
        parameters = details['parameters']
    prompt = (f"Generate positive and negative tests for this endpoint:{path} for the method {method.upper()}"
              f"considering the following specifications: "
              f"Name of the endpoint: {endpoint_name}"
              f"Request body: {request_body}"
              f"Query Parameters: {parameters} and return the tests following this template: {theme.PROMPT_TEMPLATE}")
    test_scenario = ai_connection(prompt)
    print(f"Exporting tests to file...")
    export_to_file(test_scenario, method, endpoint_name)

def ai_connection(prompt):
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text


def export_to_file(test_scenario,method,endpoint_name):
    os.makedirs("output", exist_ok=True)
    file_path = f"output/{method}_{endpoint_name}.txt"
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(test_scenario)

    print(f"Test scenario exported to file: {file_path}")



def manual_specification():
    name= input(f"Please specify the endpoint name -> ")
    path= input(f"Please specify the endpoint path -> ")
    method= input(f"Please specify the endpoint method -> ")
    query_params= input(f"Please specify the query parameters -> ")
    request_body= input(f"Please specify the request body -> ")
    authorization= input(f"Please specify the authorization -> ")
    prompt = (f"Generate positive and negative tests for this endpoint:{path} for the method {method.upper()}"
              f"considering the following specifications: "
              f"Request body: {request_body}"
              f"Query Parameters: {query_params}, authorization:{authorization} and return the tests following this template: {theme.PROMPT_TEMPLATE}")

    test_scenario = ai_connection(prompt)
    print(f"Exporting tests to file...")
    export_to_file(test_scenario, method, name)
