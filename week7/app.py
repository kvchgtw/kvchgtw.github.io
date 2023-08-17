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
    if "username" in session:
        try:
            username = request.args.get("username", None)
            #拿username去資料庫查
            
            con = mysql.connector.connect(
                                user='root',
                                password='1qaz@Wsx',
                                host='localhost',
                                database='website'
                            )
            cursor = con.cursor()
            cursor.execute("SELECT id, name, username from `member` WHERE username = %s", (username,))
            data = cursor.fetchall()
            
            if data:

                data_json = {
                            "id":data[0][0],
                            "name":data[0][1],
                            "username":data[0][2]

                        }
            else:
                data_json = None
            
            dict={"data":data_json}

        finally:
            if con.is_connected():
                cursor.close()
                con.close()
    else:
        dict={"data":None}

    response_json = json.dumps(dict, default=str)  # 將字典轉換為 JSON 格式，使用 default=str 讓 None 轉換為 null
    return response_json

  
@app.route("/api/member", methods=["PATCH"])
def updateName():
    content_type = request.headers.get('Content-Type')

    if "username" in session and content_type == 'application/json':
        try:
            username = session["username"]
            json_data = request.get_json() # 獲取前端傳來的 JSON 數據，存到json_data中            
            name = json_data.get('name') # 把新名字存到 name 中

            con = mysql.connector.connect(
            user='root',
            password='1qaz@Wsx',
            host='localhost',
            database='website'
            )

            cursor = con.cursor()
            cursor.execute("UPDATE `member` SET name = %s WHERE username = %s",(name, username))
            con.commit() #確定執行
    
            # 如果成功更新，回傳成功的 JSON 格式
            response_data = {'ok': True}
            return jsonify(response_data)
        
        except Exception as e:
            return jsonify({'error': True})
        
        finally:
            if con.is_connected():
                cursor.close()
                con.close()
    else:
        return jsonify({'error': True})
    




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
            
            

            if name:
                name = name[0]
            else:
                name = "尊敬的會員"

            return render_template("member.html", name=name)
            
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
                



@app.route("/signout")
def signout():
    del session["username"]
    return redirect("/")



app.run(port=3000) 