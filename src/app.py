from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello!"

@app.route("/hello")
def hello_world2():
    return "Hello, Sungshin2!"

@app.route("/bye")
def hello_world3():
    return "bye- bye"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
