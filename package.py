#!C:\Python311\python.exe
print("Content-Type:text/html\n\r")
import cgi
import pymysql

data=cgi.FieldStorage()
mydb=pymysql.Connect(host="localhost",user="root",password="Sachin@2106",database="travel")
cur=mydb.cursor()

c=data.getvalue("logemail")
d=data.getvalue("logpass")

cur.execute("select * from log_details")
sac=cur.fetchall()
for i in sac:
    if i[0]==c and i[1]==d:
        print('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Adventure</title>
            <link rel="stylesheet" href="package.css">
        </head>
<body>
        <div class="menu" id="Menu">
                <h1 class="heading"> our<span>packages</span></h1>
                
            <div class="menu_box">

                <div class="menu_card">

                    <div class="menu_image">
                      <img src="images/img22.jpg">
                    </div>
                    <div class="menu_info">
                        <h2>Manali-<span>4D/3N</span></h2>
                        <h2>Rs.29,999/P</h2>
                        <h3>~~> 2 Flights</h3>
                        <h3>~~> 1 Hotel</h3>
                        <h3>~~> 4d Food</h3>
                        <p>Adventure tours and travels is offerd the couples package of manali.It include the all of activities and others.It only limited people to redeem the offer book soon to get Gifts.</p>
                        <a href="booking.py" class="btn">Book Now</a>
                    </div>
                </div>    
            

                <div class="menu_card">

                    <div class="menu_image">
                     <img src="images/img25.jpg">
                    </div>
                    <div class="menu_info">
                        <h2>Kerala-<span>6D/5N</span></h2>
                        <h2>Rs.19,999/P</h2>
                        <h3>~~> 2 Flights</h3>
                        <h3>~~> 1 Hotel</h3>
 
                        <h3>~~> 5d Food</h3>
                        <p>Kerala is one of the god own country its very beautiful one.This package is include on trvel over the most of place in kerala and include the trekking, off road and see the Adenture.</p>
                        <a href="booking.py" class="btn">Book Now</a>
                    </div>
                </div>
                <div class="menu_card">

                    <div class="menu_image">
                     <img src="images/img26.jpg">
                    </div>
                    <div class="menu_info">
                        <h2>Goa-<span>3D/2N</span></h2>
                        <h2>Rs.24,500/P</h2>
                        <h3>~~> 1 Hotel</h3>
                        <h3>~~> 3d Food</h3>
                        <h3>~~> 5 Activities</h3>
                        <p>Goa is the most favorable place in most of bachlour and dream place.Adventure tours and travels is offer very lowest price to enjoy the all activities.Book Soon..</p>
                        <a href="booking.py" class="btn">Book Now</a>
                    </div>
                </div>
            </div>
        </div>
        </body>
        </html>
        ''')
        break

        
