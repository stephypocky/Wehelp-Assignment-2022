from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import session
from flask import jsonify
# 和用 json.dumps 得到的結果是一樣的，但 jsonify 的 Content-Type 是 application/json，這樣做是符合 HTTP 協議規定的，是使用 jsonify 的原因之一。
from flask import make_response
import mysql.connector
from mysql.connector import pooling
from mysql.connector import errors


dbconfig = {
    "user": "root",
    "password": "",
    "host": "localhost",
    "database": "website"
}

# Get connection object from a pool

connection_pool = mysql.connector.pooling.MySQLConnectionPool(pool_name="mypool",
                                                              pool_size=10,
                                                              pool_reset_session=True,
                                                              **dbconfig)
connection_object = connection_pool.get_connection()
mycursor = connection_object.cursor()


app = Flask(__name__, static_folder="public", static_url_path="/")
app.secret_key = '_5#y2L"F4Q8z\nc]/'
app.config['JSON_AS_ASCII'] = False  # 為了要讓json格式可以顯示中文


# 連接 MySQL 資料庫
# mydb = mysql.connector.connect(
#     host='localhost',          # 主機名稱
#     database='website',  # 資料庫名稱
#     user='root',        # 帳號
#     password='19890509',  # 密碼
# )

# 預設讀取資料的方式不會一次讀取完，當還有資料未讀取完畢就會發生錯誤，所以要設定(buffered=True)

# 首頁


@app.route("/")
def index():
    return render_template("index.html")

# 註冊


@app.route("/signup/", methods=["POST"])
def signup():
    name = request.form["name"]
    username = request.form["username"]
    password = request.form["password"]
    try:
        connection_object = connection_pool.get_connection()
        mycursor = connection_object.cursor()
        mycursor.execute(
            "SELECT * FROM member WHERE username=%s", (username,))
        myresult = mycursor.fetchone()
        if myresult != None:
            return redirect("/error?message=帳號已經被註冊")
        else:
            mycursor.execute(
                "INSERT INTO member (name, username, password) VALUES (%s, %s, %s)", (name, username, password))
            connection_object.commit()
            return redirect("/")
    except:
        print("unexpected error")

    finally:
        if connection_object.is_connected():
            mycursor.close()
            connection_object.close()


# 登入


@app.route("/signin/", methods=["POST"])
def signin():
    username = request.form["username"]
    password = request.form["password"]
    try:
        connection_object = connection_pool.get_connection()
        mycursor = connection_object.cursor()
        mycursor.execute(
            "SELECT * FROM member WHERE username=%s AND password=%s", (username, password))  # 在string裡面加variable，%s是字串值的佔位符
        myresult = mycursor.fetchone()
        if myresult == None:
            return redirect("/error?message=帳號或密碼輸入錯誤")
        else:
            session["id"] = myresult[0]
            session["name"] = myresult[1]
            session["username"] = myresult[2]  # 若是沒有先session存起來，往後要用必須在從資料庫拉出來
            return redirect("/member/")
    except:
        print("unexpected error")

    finally:
        if connection_object.is_connected():
            mycursor.close()
            connection_object.close()


# 會員頁


@app.route("/member/")
def member():
    try:
        connection_object = connection_pool.get_connection()
        mycursor = connection_object.cursor()
        mycursor.execute(
            "SELECT member.name, message.content FROM member INNER JOIN message on member.id=message.member_id;")
        myresult = mycursor.fetchall()
        if "username" in session:
            name = session["name"]
            return render_template("member.html", name=name, myresult=myresult)
        else:
            return redirect("/")
    except:
        print("unexpected error")
    finally:
        if connection_object.is_connected():
            mycursor.close()
            connection_object.close()


# 查詢會員資料


@app.route("/api/member/", methods=["GET"])
def api_member():
    username = request.args.get("username", "N/A")
    try:
        connection_object = connection_pool.get_connection()
        mycursor = connection_object.cursor()
        mycursor.execute(
            "SELECT id, name, username FROM member WHERE username=%s", (username,))
        myresult = mycursor.fetchone()
        null = None
        if myresult == None:
            return jsonify({"data": None})
        else:
            return jsonify({
                "data": {
                    "id": myresult[0],
                    "name": myresult[1],
                    "username": myresult[2]
                }
            })
    except:
        print("unexpected error")
    finally:
        if connection_object.is_connected():
            mycursor.close()
            connection_object.close()


# 修改姓名


@app.route("/api/member/", methods=["PATCH"])
def rename():
    username = session["username"]
    newname = request.get_json()["name"]  # 和前端請求回應JSON格式，{"name": "新的使⽤者姓名"}
    try:
        connection_object = connection_pool.get_connection()
        mycursor = connection_object.cursor()
        mycursor.execute(
            'UPDATE member SET name="%s" WHERE username="%s"' % (newname, username))  # 用逗號會報錯誤訊息，改用%、%s用“”包起來
        connection_object.commit()
        true = True
        if session["name"] == newname:
            return jsonify({"error": True})
        else:
            return jsonify({"ok": True})
    except:
        print("unexpected error")
    finally:
        if connection_object.is_connected():
            mycursor.close()
            connection_object.close()


@app.route("/error/")
def error():
    message = request.args.get("message", "error")  # 預設值一定要寫
    return render_template("error.html", message=message)


# 留言


@app.route("/message/", methods=["POST"])
def message():
    content = request.form["content"]
    member_id = session["id"]
    try:
        connection_object = connection_pool.get_connection()
        mycursor = connection_object.cursor()
        mycursor.execute(
            "INSERT INTO message (member_id, content) VALUES (%s, %s)", [member_id, content])
        connection_object.commit()
    except:
        print("unexpected error")
    finally:
        if connection_object.is_connected():
            mycursor.close()
            connection_object.close()

    return redirect("/member/")

# 登出


@app.route("/signout/")
def signout():
    session.pop("name", None)
    session.pop("id", None)
    session.pop("username", None)
    return redirect("/")


app.run(port=3000)
