#!C:\Python311\python.exe
print("Content-Type:text/html\n\r")
import cgi
import pymysql

data=cgi.FieldStorage()
mydb=pymysql.Connect(host="localhost",user="root",password="Sachin@2106",database="travel")
cur=mydb.cursor()

a=data.getvalue("email")
b=data.getvalue("pass")
query="insert into log_details values(%s,%s)"
values=[a,b]
cur.execute(query,values)
mydb.commit()


print('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Adventure</title>
    <link rel="stylesheet" href="studentcss.css">
</head>
<style>
body {
  background-image: url('img09.jpg');
  background-repeat: no-repeat;
  background-attachment: fixed;  
  background-size: cover;
}
</style>
<body>
    <div class="wrapper">
        <div class="form-box login">
            <h1>LogIn</h1>
            <form action="package.py" method="post">
                <div class="input-box">
                    <span class="icon">
                        <ion-icon name="mail-outline"></ion-icon>
                    </span>
                    <input Type="email"  name="logemail" required>
                    <label>Email</label>
                </div>
                <div class="input-box">
                    <span class="icon"><ion-icon name="lock-closed-outline"></ion-icon>
                    </span>
                    <input Type="password" name="logpass"required>
                    <label>Password</label>
                </div>
                <button type="submit" class="bton">LogIn</button>
        </div>
    </div>
    <script type="module" src="https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.esm.js"></script>
    <script nomodule src="https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.js"></script>

</body>
</html>
''')

