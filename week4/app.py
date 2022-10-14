from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import session


app = Flask(__name__)
app.secret_key = '_5#y2L"F4Q8z\nc]/'


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/signin/", methods=["POST"])
def signin():
    account = request.form["account"]
    password = request.form["password"]
    if account == "test" and password == "test":
        session["account"] = request.form["account"]
        return redirect("/member/")
    if account == "" or password == "":
        return redirect("/error?message=請輸入帳號密碼")
    if account != "test" or password != "test":
        return redirect("/error?message=帳號、或密碼輸入錯誤")


@app.route("/member/")
def member():
    if "account" in session:
        return render_template("member.html")
    else:
        return redirect("/")


@app.route("/error/")
def error():
    message = request.args.get("message", "error")  # 預設值一定要寫
    return render_template("error.html", message=message)
    # 變數放的順序會影響結果，所以都設一樣的


@app.route("/signout/")
def signout():
    session.pop("account", None)
    return redirect("/")


@app.route("/square/")
def calculate():
    number = request.args.get("number", "0")
    return redirect("/square/"+number)


@app.route("/square/<int:number>")
def square(number):
    squareNumber = number**2
    squareNumber = int(squareNumber)
    return render_template("square.html", squareNumber=squareNumber)


app.run(port=3000)
