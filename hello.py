from flask import Flask,render_template,request
from flask_mysqldb import MySQL
import MySQLdb.cursors
import mysql.connector

app=Flask(__name__)
app.config['MySQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'pandey21'
app.config['MYSQL_DB'] = 'pandey'

mysql = MySQL(app)

def select():
    cur=mysql.connection.cursor()
    cur.execute("select * from blogpost")
    datalist=cur.fetchall()
    mysql.connection.commit()
    cur.close()
    return datalist

@app.route('/')
def index():
    return render_template('index.html')


@app.route("/authreg" , methods=['GET' , 'POST'])
def authreg():
    if request.method == 'POST':
        name = request.form.get('name')
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        cur=mysql.connection.cursor()
        cur.execute("insert into author(name,username,emailId,password)values(%s,%s,%s,%s)" , (name,username,email,password))
        mysql.connection.commit()
        cur.close()
        return render_template("authsuccess.html")
    return render_template('authreg.html')


@app.route("/authlogin" , methods=["GET" , "POST"])
def authlogin():
    if request.method=="POST":
        cursor = mysql.connection.cursor()
        cursor.execute("select username,password from author")
        output = cursor.fetchall()
        a = []
        for i in output:
            a.append(i)
        username = request.form.get("username")
        password = request.form.get("password")
        tup = (username , password)
        if tup in a:
            return render_template("authloginsuccess.html")
        else:
            return render_template("notlogin.html")
    return render_template("authlog.html")


@app.route("/userreg" , methods=['GET' , 'POST'])
def userreg():
    if request.method == 'POST':
        name = request.form.get('name')
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        cur=mysql.connection.cursor()
        cur.execute("insert into user(name,username,emailId,password)values(%s,%s,%s,%s)" , (name,username,email,password))
        mysql.connection.commit()
        cur.close()
        return render_template("usersuccess.html")
    return render_template('userreg.html')


@app.route("/userlogin" , methods=["GET" , "POST"])
def userlogin():
    if request.method=="POST":
        cursor = mysql.connection.cursor()
        cursor.execute("select username,password from user")
        output = cursor.fetchall()
        a = []
        for i in output:
            a.append(i)
        username = request.form.get("username")
        password = request.form.get("password")
        tup = (username , password)
        if tup in a:
            return render_template("userloginsuccess.html")
        else:
            return render_template("notlogin.html")
    return render_template("userlog.html")


@app.route("/blog" , methods=["GET","POST"])
def blogpost():
    if request.method=="POST":
        username = request.form.get('username')
        post=request.form.get("post")
        cursor=mysql.connection.cursor()
        cursor.execute("insert into blogpost(username,post) values(%s,%s)" , (username,post))
        mysql.connection.commit()
        cursor.close()
        return "successful"
    return render_template("blogpost.html")

@app.route("/user" , methods=['GET','POST'])
def user():
    datalist=select()
    return render_template("user.html",data=datalist)

if __name__=="__main__":
    app.run(debug=True)


C:\Users\admin\Downloads\login.page\login\mds\venv