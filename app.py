"""
Basic Flask server application.
Simple HTTP server with a few example routes.
"""

from flask import Flask, jsonify

# Create Flask application instance
app = Flask(__name__)


@app.route('/')
def home():
    """Root endpoint - returns a welcome message."""
    return jsonify({
        'message': 'Welcome to the basic Python server!',
        'status': 'running'
    })


@app.route('/health')
def health():
    """Health check endpoint - returns server status."""
    return jsonify({
        'status': 'healthy',
        'service': 'python-basic-server'
    })


@app.route('/api/hello')
def hello():
    """Simple hello endpoint."""
    return jsonify({
        'message': 'Hello, World!'
    })


@app.route('/api/hello/<name>')
def hello_name(name):
    """Personalized hello endpoint with name parameter."""
    return jsonify({
        'message': f'Hello, {name}!'
    })


if __name__ == '__main__':
    # Run the server in debug mode
    # Debug mode enables auto-reload on code changes
    app.run(debug=True, host='0.0.0.0', port=3000)

