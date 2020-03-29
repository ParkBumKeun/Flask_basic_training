from flask import Flask, render_template, redirect, url_for,request,session
from datetime import timedelta   # 세션 타임 사용위해
app = Flask(__name__)
app.secret_key = "hello" # 시크릿 키 지정 세션안될 때! 비밀 키가 같으면 문자 그대로 여기에 문자열을 입력가능
# 세션은 시크릿 키 지정 해야함!
app.permanent_session_lifetime = timedelta(minutes=5) # timedelta(days=5)도 가능 session 영구시간 지정!

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST","GET"])
def login():
    if request.method =="POST":
        session.permanent = True # 세션 영구시간 true 설정
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("login"))



@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug =True)

'''
세션은 일시적으로 사용하는 것이므로 저장해서는 안됌!
'''

