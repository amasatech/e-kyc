# app.py
from flask import Flask, jsonify
from endpoints.validate_image import validate_image_bp 

app = Flask(__name__)

# Register the validate_image blueprint
app.register_blueprint(validate_image_bp)

# Home endpoint
@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the Image Validation API!"})

if __name__ == '__main__':
    app.run(port=5000)
