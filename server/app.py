from flask import Flask
from routes import bp

# Create the Flask application instance
app = Flask(__name__)

# Register the blueprint (routes)
app.register_blueprint(bp)

# Run the server only when this file is executed directly
if __name__ == "__main__":
    app.run(port=8000)