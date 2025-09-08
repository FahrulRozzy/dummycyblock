from flask import Flask
from flask_cors import CORS
from routes.dummy_routes import dummy_bp

def create_app():
    app = Flask(__name__)
    CORS(app)  # enable CORS

    # register blueprint
    app.register_blueprint(dummy_bp, url_prefix="/api")
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=5000)