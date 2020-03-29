from flask import Flask, render_template, redirect, url_for

app =Flask(__name__)

@app.route("/<name>")

def home(name):
    return render_template("index3.html", content=['tim', 'joe','bill'])

if __name__ == "__main__":
    app.run()