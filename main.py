from flask import Flask

app = Flask(__name__)

def bold(function):
    def wrapper():
        string = function()
        return f"<b>{string}</b"
    return wrapper

def emphasis(function):
    def wrapper():
        string = function()
        return f"<i>{string}</i>"

    return wrapper

def underline(function):
    def wrapper():
        string = function()
        return f"<u>{string}</u>"
    return wrapper



@app.route("/")
@bold
@emphasis
@underline
def home():
    return 'Hello'


@app.route("/username/<name>")
def greet(name):
    return f"hello {name}"


if __name__ == "__main__":
    app.run(debug=True)
