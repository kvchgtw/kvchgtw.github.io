from flask import *


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
    if "username" in session and session["username"] == "test":
        print(session["username"])
        return render_template("member.html")
    else:  
        return redirect("/")
        
    

#/error?msg=錯誤訊息
@app.route("/error")
def error():
    message = request.args.get("msg", "發生錯誤，請聯繫客服 ")
    return render_template("error.html", message=message)

@app.route("/signin", methods=["POST"])
def signin():
    username = request.form["username"]
    password = request.form["password"]
    if username == "test" and password == "test":
        session["username"] = "test"
        return redirect("/member")
    elif username =="" or password == "":
        return redirect("/error?msg=請輸入帳號密碼")
    else:
        return redirect("/error?msg=帳號或密碼不正確")

@app.route("/signout")
def signout():
    del session["username"]
    return redirect("/")


app.run(port=3000) 