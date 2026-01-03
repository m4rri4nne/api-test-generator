from google import genai
from dotenv import load_dotenv
import os


def test_generator(path, method, swagger_data):
    print(f"Generating tests for {method.upper()} {path}...")
    details = swagger_data["paths"][path][method]
    request_body = ""
    parameters = ""
    # Getting the name of the endpoint
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
    template = "GET /users/{id} ✔ Scenario: Retrieve a user with a valid ID   ✔ Scenario: Validate 404 for user not found  ✘ Scenario: Missing ID parameter  ✘ Scenario: Invalid format for ID "
    prompt = (f"Generate positive and negative tests for this endpoint:{path} for the method {method.upper()}"
              f"considering the following specifications: "
              f"Name of the endpoint: {endpoint_name}"
              f"Request body: {request_body}"
              f"Query Parameters: {parameters} and return the tests following this template: {template}")
    ai_connection(prompt)

def ai_connection(prompt):
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    print(response.text)