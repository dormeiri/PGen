from flask import Flask, jsonify, request
from password_options import password_options_schema
from password_generator import PasswordGenerator


app = Flask(__name__)


@app.route('/', methods=['GET'])
def generator():
    data = request.args
    opts = password_options_schema.load(data)
    generator = PasswordGenerator(opts)
    password = generator.generate()

    return password, 200
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=False)