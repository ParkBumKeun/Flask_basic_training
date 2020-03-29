from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route("/<name>")
def home(name):
    return render_template("index2.html")

if __name__ == "__main__":
    app.run()