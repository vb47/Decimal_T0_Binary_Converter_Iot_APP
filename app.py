from types import MethodType
from flask import Flask, render_template, request


def conv(x):
    y = 0
    while x!=0:
        y = y*10 + x%2
        x = x//2
    return y

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("main.html")

@app.route("/result", methods = ['POST','GET'])
def result():
    dec = 0
    if request.method == 'POST':
        result = request.form
        for key, value in result.items():
            dec = value
        
        b = conv(int(dec))
        return render_template("result.html", binary = b)


if __name__ == '__main__':
    app.run()
