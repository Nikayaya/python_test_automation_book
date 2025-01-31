## Features

Session-scoped fixtures for common setup and configurations
Mock responses for simulating API behavior without making actual HTTP calls
JSON schema validation for ensuring API responses adhere to an expected structure
Tests covering positive and negative scenarios including server errors and timeouts

## Dependencies

- pytest
- requests
- pytest-mock
- jsonschema

Install 

```bash 
 pip install pytest requests pytest-mock jsonschema
 ```

## Directory structure

├── api_tests.py         # Main test script with API tests
└── README.md            # Documentation and setup instructions

## Running Tests

To run the tests, navigate to the project directory and run the following command:

```bash 
 pip pytest api_tests.py
 ```