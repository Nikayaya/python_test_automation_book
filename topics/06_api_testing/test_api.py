"""Test suite for CRUD operations on JSONPlaceholder API"""
import pytest
import requests
from jsonschema import validate
from jsonschema.exceptions import ValidationError

URL = "http://jsonplaceholder.typicode.com"


# Fixtures with scope set to session ensures that these fixtures are initialized only once for the entire test session
@pytest.fixture(scope="session")
def base_url():
    """Returns the base URL for the API."""
    return URL


@pytest.fixture(scope="session")
def headers():
    """Returns common headers for all requests, including content type.
    Modify to include authorization headers as needed."""
    return {"Content-Type": "application/json"}


@pytest.fixture(scope="session")
def post_schema():
    """Defines the JSON schema for validating posts. Ensures API responses adhere to expected structure."""
    return {
        "type": "object",
        "properties": {
            "userId": {"type": "integer"},
            "id": {"type": "integer"},
            "title": {"type": "string"},
            "body": {"type": "string"}
        },
        "required": ["userId", "id", "title", "body"]
    }


@pytest.fixture
def new_post_data():
    """Fixture for providing new post data for testing."""
    return {
        "userId": 1,
        "title": "Test Post",
        "body": "This is a test post content."
    }


@pytest.fixture
def mock_post_response(mocker, new_post_data):
    """Mock response to simulate a successful post creation."""
    return mocker.Mock(
        ok=True,
        status_code=201,
        json=lambda: {**new_post_data, "id": 101}
    )


@pytest.fixture
def mock_response_failure(mocker):
    """Mock response to simulate a server failure."""
    return mocker.Mock(ok=False, status_code=500, json=lambda: {"error": "Server Error"})


@pytest.fixture
def mock_response_invalid(mocker):
    """Mock response to simulate an invalid data response from the server."""
    return mocker.Mock(ok=True, status_code=200, json=lambda: {"title": "Incomplete data"})


@pytest.fixture
def mock_timeout(mocker):
    """Mock timeout scenario using `requests.get`."""
    return mocker.patch('requests.get', side_effect=requests.exceptions.Timeout)


#Positive Tests
def test_get_post_by_id(base_url, headers, post_schema, mocker):
    """Test successful GET request for a specific post"""
    mock_response = mocker.Mock(
        ok=True,
        status_code=200,
        json=lambda: {
            "userId": 1,
            "id": 1,
            "title": "Test Post",
            "body": "Test content"
        }
    )
    mocker.patch('requests.get', return_value=mock_response)

    response = requests.get(f"{base_url}/posts/1", headers=headers)

    assert response.status_code == 200
    validate(instance=response.json(), schema=post_schema)
    assert response.json()["id"] == 1


def test_create_post(base_url, headers, post_schema, mock_post_response, mocker, new_post_data):
    """Test successful POST request to create new post"""
    mocker.patch('requests.post', return_value=mock_post_response)

    response = requests.post(f"{base_url}/posts", headers=headers, json=new_post_data)

    assert response.status_code == 201
    validate(instance=response.json(), schema=post_schema)
    assert response.json()["title"] == new_post_data["title"]
    assert response.json()["id"] == 101  # Verify server-generated ID


def test_update_post(base_url, headers, post_schema, mocker):
    """Test successful PUT request to update existing post"""
    updated_data = {
        "title": "Updated Title",
        "body": "Updated body content"
    }
    mock_response = mocker.Mock(
        ok=True,
        status_code=200,
        json=lambda: {
            "userId": 1,
            "id": 1,
            **updated_data
        }
    )
    mocker.patch('requests.put', return_value=mock_response)

    response = requests.put(f"{base_url}/posts/1", headers=headers, json=updated_data)

    assert response.status_code == 200
    validate(instance=response.json(), schema=post_schema)
    assert response.json()["title"] == updated_data["title"]


def test_delete_post(base_url, headers, mocker):
    """Test successful DELETE request"""
    mock_response = mocker.Mock(
        ok=True,
        status_code=200,
        json=lambda: {}
    )
    mocker.patch('requests.delete', return_value=mock_response)

    response = requests.delete(f"{base_url}/posts/1", headers=headers)

    assert response.status_code == 200
    assert response.json() == {}


#  Negative Tests
def test_server_error(base_url, headers, mock_response_failure, mocker):
    """Test server error handling"""
    mocker.patch('requests.get', return_value=mock_response_failure)
    response = requests.get(f"{base_url}/posts/1", headers=headers)

    assert response.status_code == 500
    assert not response.ok
    assert "error" in response.json()


def test_invalid_data_response(base_url, headers, post_schema, mock_response_invalid, mocker):
    """Test schema validation failure"""
    mocker.patch('requests.get', return_value=mock_response_invalid)
    response = requests.get(f"{base_url}/posts/1", headers=headers)

    with pytest.raises(ValidationError) as excinfo:
        validate(instance=response.json(), schema=post_schema)
    assert "required" in str(excinfo.value)


def test_timeout_error(base_url, headers, mock_timeout):
    """Test network timeout handling"""
    with pytest.raises(requests.exceptions.Timeout):
        requests.get(f"{base_url}/posts/1", headers=headers, timeout=0.1)


def test_update_non_existing_post(base_url, headers, mocker):
    """Test updating non-existing resource"""
    mock_response = mocker.Mock(
        ok=False,
        status_code=404,
        json=lambda: {"error": "Not Found"}
    )
    mocker.patch('requests.put', return_value=mock_response)

    response = requests.put(f"{base_url}/posts/999", headers=headers, json={"title": "Test"})

    assert response.status_code == 404
    assert not response.ok



if __name__ == "__main__":
    pytest.main()
