from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("base_index.html", content = "Testing")

if __name__=="__main__":
    app.run(debug=True) # 디버그 트루 지정하면 변경 될 때마다 서버를 다시 실행할 필요가 없음!
