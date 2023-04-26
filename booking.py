#!C:\Python311\python.exe
print("Content-Type:text/html\n\r")

import cgi
import pymysql

mydb=pymysql.Connect(host="localhost",user="root",password="Sachin@2106",database="book")
cur=mydb.cursor()

print('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Booking Travel</title>
    <link rel="stylesheet" href="booking.css">
</head>
<body>
        <div class="container">
            <div class="title">Book Your Trip!</div>
            <form action="booking_verify.py" method="post">
                <div class="user-details">
                    <div class="input-box">
                        <span class="details">Full Name  :</span>
                        <input type="text" placeholder="Enter Your Name" required name="name">
                    </div>
                    <div class="input-box">
                        <span class="details">Ph No      :</span>
                        <input type="text" placeholder="Enter Your Phone No" required name="phone">
                    </div>
                    <div class="input-box">
                        <span class="details">Alter Ph No:</span>
                        <input type="text" placeholder="Enter Your Alter Ph No" required name="pno">
                    </div>
                    <div class="input-box">
                        <span class="details">Email      :</span>
                        <input type="text" placeholder="Enter Your Email:" required name="email">
                    </div>
                    <div class="input-box">
                        <span class="details">Address    :</span>
                        <input type="text" placeholder="Enter Your Address" required name="address"> 
                    </div>
                    <div class="input-box">
                        <span class="details">How Many   :</span>
                        <input type="number" placeholder="Number of guests" required name="member">
                    </div>
                    <div class="inputBox">
                        <span>Arrivals date:</span>
                        <input type="date" name="arrivals">
                    </div>
                    <div class="inputBox">
                        <span>Leaving date:</span>
                        <input type="date" name="Leaving">
                    </div>
                </div>
                <div class="button">
                    <input type="submit" value="Submit">
                </div>
            </form>
        </div>
    </div> 	
          
</body>
</html>
''')


