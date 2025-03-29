from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the root URL ("/")
@app.route('/')
def hello_world():
    """This function handles requests to the root URL and returns 'Hello, World!'."""
    return "Hello, World!"

# Define a route for "/api/hello"
@app.route('/api/hello')
def hello_api():
    """This function handles requests to '/api/hello' and returns a message."""
    return "Hello, API World!"

# This part is mainly for local testing
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000, debug=True)