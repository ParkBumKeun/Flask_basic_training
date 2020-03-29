from flask import Flask, render_template, redirect, url_for,request,session, flash
from datetime import timedelta   # 세션 타임 사용위해
from flask_sqlalchemy import SQLAlchemy


'''
세션은 일시적으로 사용하는 것이므로 저장해서는 안됌!
'''


app = Flask(__name__)
app.secret_key = "hello" # 시크릿 키 지정 세션안될 때! 비밀 키가 같으면 문자 그대로 여기에 문자열을 입력가능
# 세션은 시크릿 키 지정 해야함!
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # 이렇게 하면 추적하지 않음.
app.permanent_session_lifetime = timedelta(minutes=5) # timedelta(days=5)도 가능 session 영구시간 지정!

db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key = True)
#    name = db.Column("name",db.String(100))
#    email = db.Column("email",db.String(100))
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self,name,email):
        self.name = name
        self.email = email

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/view")
def view():
    return render_template("view.html", values= users.query.all())

@app.route("/login", methods=["POST","GET"])
def login():
    if request.method =="POST":
        session.permanent = True # 세션 영구시간 true 설정
        user = request.form["nm"]
        session["user"] = user

        found_user = users.query.filter_by(name=user).first()

        if found_user:
            session["email"] = found_user.email
        else:
            usr = users(user, "")
            db.session.add(usr)
            db.session.commit()



        flash("Login Successful!")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already Logged in!")
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route("/user", methods=["POST","GET"])
def user():
    email = None
    if "user" in session:
        user = session["user"]

        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            found_user = users.query.filter_by(name=user).first()
            found_user.email = email
            db.session.commit()
            flash("Email was saved!")
        else:
            if "email" in session:
                email = session["email"]

        #return render_template("user.html", user=user)

        return render_template("user.html", email=email)
    else:
        flash("You are not logged in!")
        return redirect(url_for("login"))



@app.route("/logout")
def logout():
    # if "user" in session:
    #     user = session["user"]
    #     flash("You have been logged out", "info")
    flash("You have been logged out", "info")
    session.pop("user", None)
    session.pop("email", None)
    return redirect(url_for('login'))

if __name__ == "__main__":
    db.create_all()
    app.run(debug =True)

'''
세션은 일시적으로 사용하는 것이므로 저장해서는 안됌!
'''

