from flask import Flask, jsonify, send_file

app = Flask(__name__)

@app.route('/')
def home():
    return send_file('doc/index.html')

if __name__ == "__main__":
    app.run(debug=True)