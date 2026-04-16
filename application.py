from flask import Flask, jsonify

application = Flask(__name__)

@application.route("/")
def home():
    return jsonify(message="API running...")

@application.route("/health")
def health():
    return jsonify(status="ok")

if __name__ == '__main__':
    application.run(debug=True, host='0.0.0.0', port=5000)