from flask import Blueprint, render_template

second = Blueprint("second", __name__, static_folder = 'static', template_folder= 'templates') # 변수와 Blueprint("예로한 second[=변수명과 같아야 좋음!"] )

@second.route("/home")

@second.route("/")
def home():
    return render_template("home.html")

@second.route("/test")
def test():
    return"<h1>admin</h1>"
