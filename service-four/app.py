from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "4️⃣ This is service four"


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
