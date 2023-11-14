from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/account", methods=["GET", "POST"])
def account():
    if request.method == "POST":
        user = request.form["user"]
        pwd = request.form["pwd"]
        result = "您輸入的帳號是：" + user + "; 密碼為：" + pwd 
        return result
    else:
        return render_template("account.html")


@app.route("/")
def index():
    homepage = "<h1>資管二B楊承恩求職資訊1114</h1>"
    homepage += "<a href=/today>相關工作介紹</a><br>"
    homepage += "<a href=/welcome?nick=楊子青>傳送使用者暱稱</a><br>"
    homepage += "<a href=/about>職涯測驗結果</a><br>"
    homepage += "<a href=/account>履歷自傳</a><br>"
    return homepage


@app.route("/mis")
def course():
    return "<h1>資訊管理導論</h1>"

@app.route("/today")
def today():
    now = datetime.now()
    return render_template("today.html",datetime = str(now))

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/welcome", methods=["GET", "POST"])
def welcome():
    user = request.values.get("nick")
    return render_template("welcome.html", name=user)


#if __name__ == "__main__":
 #   app.run()