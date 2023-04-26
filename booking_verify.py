#!C:\Python311\python.exe
print("Content-Type:text/html\n\r")

import cgi
import pymysql

data=cgi.FieldStorage()
mydb=pymysql.Connect(host="localhost",user="root",password="Sachin@2106",database="book")
cur=mydb.cursor()

a=data.getvalue("name")
b=data.getvalue("phone")
c=data.getvalue("email")
d=data.getvalue("address")
e=data.getvalue("member")
f=data.getvalue("arrivals")
g=data.getvalue("Leaving")


query="insert into book_details values(%s,%s,%s,%s,%s,%s,%s)"
values=[a,b,c,d,e,f,g]
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
        </head>
        <style>
        body{
        background-image: url('img06.jpg');
        background-repeat: no-repeat;
        background-attachment: fixed;  
        background-size: cover;
        }
        nav{
    	display: flex;
    	align-items: center;
    	justify-content: space-between;
    	padding-top: 45px;
    	padding-left: 8%;
    	padding-right: 8%;
        }

        .logo{
    	color: white;
    	font-size: 35px;
	letter-spacing: 1px;
	cursor: pointer;
	text-decoration: none;
        }
        span{
    	color: gold;
        }
        nav ul li{
    	list-style-type: none;
    	display: inline-block;
    	padding: 10px 25px;
        }
        nav ul li a{
    	color: white;
    	text-decoration: none;
    	font-weight: bold;
    	text-transform: capitalize;
        }
        nav ul li a:hover{
	color: #f9004d;
    	transition: .4s;
        }
        .block{
         position: relative;
         width: 800px;
         height: 400px;
         right:-250px;
         top:-10px;
         color: white;
         background: transparent;
         border: 2px solid rgba(255, 255, 255, .5);
         border-radius: 20px;
         backdrop-filter: blur(20px);
         box-shadow: 0 0 30px rgba(0, 0, 0, .5);
        
         }
         .block .form-box{
	  width: 100%;
	  padding: 40px;
	  }
          .btn{
            width: 10%;
            height: 45px;
            background: white;
            border: 2px solid transparent;
            font-weight: bold;
            font-size: 1rem;
            color: black;
            cursor: pointer;
            padding: 10px 10px;
            margin: 2px 580px;
            border-radius: 30px;
            transition: transform.4s;
            }
            .btn:hover{
             transform: scale(1.2);
            }
        </style>
        </html>

      <body>
       <div class="course">
        <nav>
          <a href="#" class="logo"><i class="fas fa-hiking"></i>Adventure</a>
          <ul>
            <li><a class="active" href="home.html">Home</a></li>
            <li><a href="#about">Service</a></li>
            <li><a href="#services">About</a></li>
            <li><a href="#contact">Contact</a></li>
            <li><a href="home.html">Logout</a></li>
          </ul>
        </nav>
            <div class="block">
	      <h1><center><ins><span>Congratulation.....!</span></ins> <br><br>Your trip is sucessfully booked!</center></h1><br>
	      <h2><center>Thank you for choose our trip package 
	      <br>other details will be shared by your Email...!</center></h2><br>
	      <h2><center>Enjoy the<span> Tour and be Safe....!</span></center></h2>
	    </div>
       </div>
''')
