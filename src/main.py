from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello, Flask!</h1>"

@app.route("/test")
def test():
    return "test"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
