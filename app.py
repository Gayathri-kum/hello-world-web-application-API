from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello!'

@app.route('/healthz')
def health():
    status = {
        "status": "OK",
        "version": "0.0.1",
        "uptime": "up since 2020-08-04 08:00:05"
    }
    return jsonify(status)

if __name__ == "__main__":
    app.run(port=8080,host='0.0.0.0')
