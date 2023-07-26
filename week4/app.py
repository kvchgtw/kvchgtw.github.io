from flask import *
from werkzeug.serving import *
import threading


app=Flask(
    __name__,
    static_folder="public",
    static_url_path="/"   
          ) #建立 application 物件
app.secret_key="any string but secret"

#建立網站首頁的回應方式
@app.route("/")
def index(): #用來回應網站首頁連線的函式
    return render_template("index.html")   #回傳的內容


#啟動網站伺服器可透過 port 指定埠號
@app.route("/member")
def member():
    return render_template("member.html")

@app.route("/error/<errormsg>")
def error():
    return render_template("error.html")

#動態路由
@app.route("/user/<username>")
def handleuser(username):
    return "Hello" + username 



app.run(port=3000) 