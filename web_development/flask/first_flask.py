from flask import Flask

# Create the Flask app
app = Flask(__name__)

# Define a route and its view function
@app.route('/')
def home():
    return "Hello, Flask! Your server is running. 🎉"

# Run the server
if __name__ == '__main__':
    app.run(debug=True)