from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import session
import mysql.connector


app = Flask(__name__, static_folder="public", static_url_path="/")
app.secret_key = '_5#y2L"F4Q8z\nc]/'

# 連接 MySQL 資料庫
mydb = mysql.connector.connect(
    host='localhost',          # 主機名稱
    database='website',  # 資料庫名稱
    user='root',        # 帳號
    password='',  # 密碼
)
mycursor = mydb.cursor(buffered=True)
# 預設讀取資料的方式不會一次讀取完，當還有資料未讀取完畢就會發生錯誤，所以要設定(buffered=True)


@app.route("/")
def index():
    return render_template("index.html")

# 註冊


@app.route("/signup/", methods=["POST"])
def signup():
    name = request.form["name"]
    username = request.form["username"]
    password = request.form["password"]
    mycursor.execute(
        "SELECT * FROM member WHERE username=%s", [username])  # 在string裡面加variable，%s是字串值的佔位符
    myresult = mycursor.fetchone()
    if myresult != None:
        return redirect("/error?message=帳號已經被註冊")
    else:
        mycursor.execute(
            "INSERT INTO member (name, username, password) VALUES (%s, %s, %s)", [name, username, password])
        mydb.commit()
        return redirect("/")

# 登入


@app.route("/signin/", methods=["POST"])
def signin():
    username = request.form["username"]
    password = request.form["password"]
    mycursor.execute(
        "SELECT * FROM member WHERE username=%s AND password=%s", [username, password])  # 在string裡面加variable，%s是字串值的佔位符
    # 前面的 username/password 指的是 mysql 裡的
    # 後面的 username/password 指的是 前端傳入的
    myresult = mycursor.fetchone()
    if myresult == None:
        return redirect("/error?message=帳號或密碼輸入錯誤")
    else:
        session["id"] = myresult[0]
        session["name"] = myresult[1]
        return redirect("/member/")


@app.route("/member/")
def member():
    username = request.args.get("username", "N/A")
    password = request.args.get("password", "N/A")
    mycursor.execute(
        "SELECT member.name, message.content FROM member INNER JOIN message on member.id=message.member_id;")
    myresult = mycursor.fetchall()
    if "username" in session:
        name = session["name"]
        return render_template("member.html", name=name, myresult=myresult)
    else:
        return redirect("/")


@app.route("/error/")
def error():
    message = request.args.get("message", "error")  # 預設值一定要寫
    return render_template("error.html", message=message)
    # 變數放的順序會影響結果，所以都設一樣的

# 留言


@app.route("/message/", methods=["POST"])
def message():
    content = request.form["content"]
    member_id = session["id"]
    mycursor.execute(
        "INSERT INTO message (member_id, content) VALUES (%s, %s)", [member_id, content])
    mydb.commit()
    return redirect("/member/")


# 登出


@app.route("/signout/")
def signout():
    session.pop("name", None)
    session.pop("id", None)
    return redirect("/")


app.run(port=3000)
