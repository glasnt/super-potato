from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "2️⃣ This is service two"


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
