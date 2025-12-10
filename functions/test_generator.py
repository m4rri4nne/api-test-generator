

def test_generator(path, method, swagger_data):
    print(f"Generating tests for {method.upper()} {path}...")

    details = swagger_data["paths"][path][method]
    print(details['responses'])
    



def file_generator(path,method):
    print(f"Generating files for {method.upper()} {path}...")
    # Here you would add the logic to generate the actual files
    # based on the path and method provided.
    print(f"Files generated for {method.upper()} {path}!\n")