from flask import Flask, render_template, request, jsonify, session
from flask_cors import CORS

app = Flask(__name__, static_folder='static')
CORS(app)

@app.route('/')
def index():
    return render_template('./index.html')


if __name__ == '__main__':
    app.run(debug=True)
