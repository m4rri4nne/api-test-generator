# 🚀 API Test Generator

A powerful tool designed to help QAs and engineering teams automatically generate API test scenarios directly from a Swagger/OpenAPI specification.
Reduce manual work, improve test coverage, and optionally push approved test cases to Zephyr.

## 📘 Description
The API Test Generator automates the process of discovering, parsing, and transforming Swagger definitions into actionable test scenarios.
It provides:
-  Automatic extraction of endpoints, parameters, and responses
-  Auto-generated positive and negative test cases
-  Human approval flow for each scenario
-  Export of approved tests to a local file
-  Optional integration with Zephyr to create test items directly
-  Perfect for QA engineers, SDETs, and API testing workflows

## 🔧 Technologies

- Python 3.x
- Swagger/OpenAPI parsing
- Optional Zephyr API integration
- Rich CLI support (e.g., typer, rich)
- JSON/YAML processing

## 📂 How It Works
1. You provide a Swagger URL or local file.
2. The system validates and loads the specification.
3. Test scenarios are automatically generated from the API structure:
    - Positive cases
    - Negative/error cases
    - Missing/invalid parameter cases
    - Status code–based cases
4. You review and approve each scenario.
5. Approved test cases are saved locally.
6. (Optional) You can export them automatically to Zephyr.


### Using the application

Create a new virtual environment and activate the virtual environement:

Windows or Powershell: 

```bash
 python -m venv env_name
```

Linux or Mac: 
```bash
 python3 -m venv env_name
```

Activating the environement on Windows(cmd): 

```bash
 env_name\Scripts\activate
```

Activating the environement on Linux/Mac: 
```bash
 source env_name/bin/activate
```

Install the dependencies from `requirements.txt` file: 

```bash
 pip install -r requirements.txt
```

### 📝 Example Output

```bash
GET /users/{id}
✔ Scenario: Retrieve a user with a valid ID  
✔ Scenario: Validate 404 for user not found  
✘ Scenario: Missing ID parameter  
✘ Scenario: Invalid format for ID  
```

## 🤝 Contributing
Pull Requests are welcome!
For major changes, please open an issue to discuss what you would like to modify.

## 📄 License
This project is licensed under the MIT License.
