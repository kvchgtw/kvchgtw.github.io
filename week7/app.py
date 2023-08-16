from flask import *
import mysql.connector



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

@app.route("/api/member")
def apiMember(): #用來回應網站首頁連線的函式
    data = request.args.
    return render_template("index.html")   #回傳的內容


#啟動網站伺服器可透過 port 指定埠號
@app.route("/member")
def member():
    if "username" in session:
        username = session["username"]
        try:
            con = mysql.connector.connect(
                    user='root',
                    password='1qaz@Wsx',
                    host='localhost',
                    database='website'
                )

            cursor = con.cursor()
            cursor.execute("SELECT name from `member` WHERE username = %s", (username,))
            name = cursor.fetchone()
            cursor.execute("SELECT name, content FROM `member` INNER JOIN message ON `member`.id=message.member_id;")
            message = cursor.fetchall()
            
            messages=[]

            for messageName, content in message:
                displayMessage = f"{messageName}: {content}"
                messages.append(displayMessage)
            

            if name:
                name = name[0]
            else:
                name = "尊敬的會員"

            return render_template("member.html", name=name, messages=messages)
            
        finally:
            if con.is_connected():
                cursor.close()
                con.close()
    else:  
        return redirect("/")
    
    

            
        
        
    

#/error?msg=錯誤訊息
@app.route("/error")
def error():
    message = request.args.get("msg", "發生錯誤，請聯繫客服 ")
    return render_template("error.html", message=message)

@app.route("/signin", methods=["POST"])
def signin():
    if request.method=='POST':
        username = request.form["username"]
        password = request.form["password"]
    try:   

        con = mysql.connector.connect(
            user='root',
            password='1qaz@Wsx',
            host='localhost',
            database='website'
            )

        cursor = con.cursor()
        cursor.execute("SELECT username from `member` WHERE username = %s AND password =%s", (username, password))
        existing_user = cursor.fetchone()
    

   
        if existing_user:
            session["username"] = username
            return redirect("/member")
     
        else:
            return redirect("/error?msg=帳號或密碼不正確")
    finally:
        if con.is_connected():
                cursor.close()
                con.close()
                
    
@app.route("/signup", methods=["POST"])
def signup():

    if request.method=='POST':

        name = request.form["name"]
        username = request.form["username"]
        password = request.form["password"]

        try:

            con = mysql.connector.connect(
            user='root',
            password='1qaz@Wsx',
            host='localhost',
            database='website'
            )

            cursor = con.cursor()
            cursor.execute("SELECT username from `member` WHERE username = %s", (username,))
            existing_user = cursor.fetchone()

            if existing_user:
                return redirect("/error?msg=此帳號已被註冊，請使用其他帳號註冊")
            
            
            cursor.execute("INSERT INTO `member` (name, username, password) VALUES (%s, %s, %s)", (name, username, password))

            con.commit() #確定執行
            return redirect("/")
        finally:
            if con.is_connected():
                cursor.close()
                con.close()
                
@app.route("/createMessage", methods = ["POST"])
def createMessage():
    if "username" in session:
        username = session["username"]
        content = request.form["content"]
        
        try:

            con = mysql.connector.connect(
            user='root',
            password='1qaz@Wsx',
            host='localhost',
            database='website'
            )

            cursor = con.cursor()
            cursor.execute("SELECT id from `member` WHERE username = %s", (username,))
            existing_id = cursor.fetchone()
            
            if existing_id:
                existing_id = existing_id[0]
                cursor.execute("INSERT INTO message (member_id, content) VALUES (%s, %s)", (existing_id,content))
                con.commit()
                cursor.execute("SELECT username, content FROM `member` INNER JOIN message ON `member`.id=message.member_id;")
                


        finally:
            if con.is_connected():
                cursor.close()
                con.close()

    


@app.route("/signout")
def signout():
    del session["username"]
    return redirect("/")


app.run(port=3000) 