from marshmallow import ValidationError
from flask import Flask, jsonify, request
from flask_cors import CORS
from password_options import password_options_schema
from password_generator import PasswordGenerator


app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def generator():
    try:
        data = request.args
        opts = password_options_schema.load(data)
        generator = PasswordGenerator(opts)
        password = generator.generate()

        return jsonify(password), 200
        
    except ValidationError as err:
        return err.messages, 400
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=False)