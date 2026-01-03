# Python Basic Server

A simple Flask-based HTTP server with basic REST endpoints.

## Setup

1. Activate the virtual environment:

```bash
source .venv/bin/activate
```

2. Install dependencies (if not already installed):

```bash
pip install -r requirements.txt
```

## Running the Server

```bash
python app.py
```

The server will start on `http://localhost:3000`

## Running Tests

Run all tests:

```bash
pytest
```

Run tests with verbose output:

```bash
pytest -v
```

Run a specific test file:

```bash
pytest tests/test_app.py
```

Run a specific test class or test method:

```bash
pytest tests/test_app.py::TestRootEndpoint
pytest tests/test_app.py::TestRootEndpoint::test_root_endpoint_returns_200
```

The test suite includes 16 tests covering all endpoints, status codes, JSON responses, and edge cases.

## Linting and Formatting

### Linting with flake8

Check code for style and quality issues:

```bash
flake8 app.py tests/
```

Check specific files or directories:

```bash
flake8 app.py
flake8 tests/
```

### Formatting with black

Check if code needs formatting (without making changes):

```bash
black --check app.py tests/
```

Format code automatically:

```bash
black app.py tests/
```

Format all Python files in the project:

```bash
black .
```

**Note:** Configuration files (`.flake8` and `pyproject.toml`) are already set up with appropriate settings.

## Available Endpoints

- `GET /` - Welcome message
- `GET /health` - Health check endpoint
- `GET /api/hello` - Simple hello message
- `GET /api/hello/<name>` - Personalized hello message

## Example Requests

```bash
# Root endpoint
curl http://localhost:3000/

# Health check
curl http://localhost:3000/health

# Hello endpoint
curl http://localhost:3000/api/hello

# Personalized hello
curl http://localhost:3000/api/hello/John
```
