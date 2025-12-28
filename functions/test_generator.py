

def test_generator(path, method, swagger_data):
    print(f"Generating tests for {method.upper()} {path}...")
    details = swagger_data["paths"][path][method]

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


    print(f'Retrive {endpoint_name} with ')


    for response in details['responses']:
        print(response)
    



def file_generator(path,method):
    print(f"Generating files for {method.upper()} {path}...")
    # Here you would add the logic to generate the actual files
    # based on the path and method provided.
    print(f"Files generated for {method.upper()} {path}!\n")