"""
Unit tests for the Flask application.
Tests all endpoints and their responses.
"""

import pytest
from app import app


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    # Create a test client using Flask's test_client
    with app.test_client() as client:
        # Set up test context
        yield client


class TestRootEndpoint:
    """Tests for the root endpoint '/'."""

    def test_root_endpoint_returns_200(self, client):
        """Test that root endpoint returns 200 status code."""
        response = client.get('/')
        assert response.status_code == 200

    def test_root_endpoint_returns_json(self, client):
        """Test that root endpoint returns JSON content."""
        response = client.get('/')
        assert response.is_json is True

    def test_root_endpoint_message(self, client):
        """Test that root endpoint returns correct message."""
        response = client.get('/')
        data = response.get_json()
        assert data['message'] == 'Welcome to the basic Python server!'
        assert data['status'] == 'running'


class TestHealthEndpoint:
    """Tests for the health check endpoint '/health'."""

    def test_health_endpoint_returns_200(self, client):
        """Test that health endpoint returns 200 status code."""
        response = client.get('/health')
        assert response.status_code == 200

    def test_health_endpoint_returns_json(self, client):
        """Test that health endpoint returns JSON content."""
        response = client.get('/health')
        assert response.is_json is True

    def test_health_endpoint_status(self, client):
        """Test that health endpoint returns correct status."""
        response = client.get('/health')
        data = response.get_json()
        assert data['status'] == 'healthy'
        assert data['service'] == 'python-basic-server'


class TestHelloEndpoint:
    """Tests for the hello endpoint '/api/hello'."""

    def test_hello_endpoint_returns_200(self, client):
        """Test that hello endpoint returns 200 status code."""
        response = client.get('/api/hello')
        assert response.status_code == 200

    def test_hello_endpoint_returns_json(self, client):
        """Test that hello endpoint returns JSON content."""
        response = client.get('/api/hello')
        assert response.is_json is True

    def test_hello_endpoint_message(self, client):
        """Test that hello endpoint returns correct message."""
        response = client.get('/api/hello')
        data = response.get_json()
        assert data['message'] == 'Hello, World!'


class TestHelloNameEndpoint:
    """Tests for the personalized hello endpoint '/api/hello/<name>'."""

    def test_hello_name_endpoint_returns_200(self, client):
        """Test that hello name endpoint returns 200 status code."""
        response = client.get('/api/hello/John')
        assert response.status_code == 200

    def test_hello_name_endpoint_returns_json(self, client):
        """Test that hello name endpoint returns JSON content."""
        response = client.get('/api/hello/John')
        assert response.is_json is True

    def test_hello_name_basic(self, client):
        """Test hello name endpoint with a simple name."""
        response = client.get('/api/hello/John')
        data = response.get_json()
        assert data['message'] == 'Hello, John!'

    def test_hello_name_different_name(self, client):
        """Test hello name endpoint with a different name."""
        response = client.get('/api/hello/Jane')
        data = response.get_json()
        assert data['message'] == 'Hello, Jane!'

    def test_hello_name_with_spaces(self, client):
        """Test hello name endpoint with name containing spaces."""
        # URL encoding: space becomes %20
        response = client.get('/api/hello/John%20Doe')
        data = response.get_json()
        assert data['message'] == 'Hello, John Doe!'

    def test_hello_name_special_characters(self, client):
        """Test hello name endpoint with special characters."""
        response = client.get('/api/hello/John-Doe')
        data = response.get_json()
        assert data['message'] == 'Hello, John-Doe!'

    def test_hello_name_empty_string(self, client):
        """Test hello name endpoint with empty string (edge case)."""
        # Empty string in URL path
        response = client.get('/api/hello/')
        # This should return 404 since the route expects a name parameter
        assert response.status_code == 404

