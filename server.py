from flask import Flask
import random

app = Flask(__name__)
number = random.randint(0, 9)


@app.route("/")
def home():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<div style="width:100%;height:0;padding-bottom:78%;position:relative;"><iframe src="https://giphy.com/embed/Nw8z2olm0nGHC" width="100%" height="100%" style="position:absolute" frameBorder="0" class="giphy-embed" allowFullScreen></iframe></div>' \
           '<p><a href="https://giphy.com/gifs/press-conference-Nw8z2olm0nGHC">via GIPHY</a></p>'


@app.route("/<int:num>")
def fun1(num):
    value = num
    if value is None:
        return '<h1>Please provide a number.</h1>'

    if abs(value - number) > 5:
        return '<h1 style="color:red">OMG TOO FAR AWAY</h1>' \
               '<div style="width:100%;height:0;padding-bottom:57%;position:relative;"><iframe src="https://giphy.com/embed/3hd24g3BYq5MY" width="100%" height="100%" style="position:absolute" frameBorder="0" class="giphy-embed" allowFullScreen></iframe></div><p><a href="https://giphy.com/gifs/excited-kermit-3hd24g3BYq5MY">via GIPHY</a></p>'
    elif abs(value - number) > 3:
        return '<h1 style="color:blue">Coming closer, try again!</h1>' \
               '<div style="width:100%;height:0;padding-bottom:56%;position:relative;"><iframe src="https://giphy.com/embed/uBtRKuhFqawxi" width="100%" height="100%" style="position:absolute" frameBorder="0" class="giphy-embed" allowFullScreen></iframe></div><p><a href="https://giphy.com/gifs/the-muppets-uBtRKuhFqawxi">via GIPHY</a></p>'
    elif abs(value - number) >= 1:
        return '<h1 style="color:yellow">VERY CLOSE!</h1>' \
               '<div style="width:100%;height:0;padding-bottom:57%;position:relative;"><iframe src="https://giphy.com/embed/xTiN0vyCvNjFJbApc4" width="100%" height="100%" style="position:absolute" frameBorder="0" class="giphy-embed" allowFullScreen></iframe></div><p><a href="https://giphy.com/gifs/kermit-the-frog-xTiN0vyCvNjFJbApc4">via GIPHY</a></p>'
    else:
        return '<h1 style="color:green">WOOHOO YOU GUESSED IT!</h1>' \
               '<div style="width:100%;height:0;padding-bottom:120%;position:relative;"><iframe src="https://giphy.com/embed/etOX3h7ApZuDe7Fc5w" width="100%" height="100%" style="position:absolute" frameBorder="0" class="giphy-embed" allowFullScreen></iframe></div><p><a href="https://giphy.com/gifs/dancing-kermit-etOX3h7ApZuDe7Fc5w">via GIPHY</a></p>'


if __name__ == "__main__":
    app.run()
