import mysql.connector
from mysql.connector import errorcode
try:
	cnn=mysql.connector.connect(
		user='root',
		password='tinni123',
		host='localhost',
                database='mobileshop')
	print ("it works!!!!")
except mysql.connector.Error as e:
    if e.errno== errorcode.ER_ACCESS_DENIED_ERROR:
        print("something is wrong")
    elif e.errno==errorcode.ER_BAD_DB_ERROR:
        print("no database")
    else:
        print(e)
        
print("WELCOME TO PHONE CRAFT MOBILE SHOP!")
mydb=cnn.cursor()
#searching for mobiles
def search():
    print("Hello! Welcome to the shop!")
    print("these are the phones we have:")
    sqlite = """SELECT sno,mobile_name,price from mobile_shop order by sno asc"""
    mydb.execute(sqlite)
    records = mydb.fetchall()
    for r in records:
        print("Serial number=",r[0])
        print("Mobile_name=", r[1])
        print("Price= ", r[2])
        print("\n")
    
    sno= input("PLEASE ENTER THE SERIAL NUMBER OF THE PHONE YOU ARE LOOKING FOR (THIS IS JUST FOR SHOWING YOU THE DETAILS OF YOUR FAVOURITE PHONES)")
    mydb.execute(f"SELECT * FROM mobile_shop WHERE sno={sno}")
    results=mydb.fetchall()
    for row in results:
        print("Serial number=",row[0])
        print("\n")
        print("Mobile_name=", row[1])
        print("Price= ", row[2])
        print("\n")
        print("Operating_system= ", row[3])
        print("\n")
        print("Memory_storage_sim=", row[4])
        print("\n")
        print("Camera=", row[5])
        print("\n")
        print("Battery= ", row[6])
        print("\n")
        print("Processor=", row[7])
        print("\n")
        print("Display_features=", row[8])
        print("\n")
        print("Display_technology=", row[9])
        print("\n")
        print("Warranty=", row[10])
        print("\n")
        print("With_the_box=", row[11])
        print("\n")
        print("Model_no=", row[12])
        print("\n")
    cnn.commit()

mydb=cnn.cursor()    
    
#shopping 
def shopping():
    while True:
        a=input("do you want to look for more phones?Y/N OR y/n")
        if a=="Y" or a=="y":
            sno= input("PLEASE ENTER THE SERIAL NUMBER OF THE PHONE YOU ARE LOOKING FOR (THIS IS JUST FOR SHOWING YOU THE DETAILS OF YOUR FAVOURITE PHONES)")
            mydb.execute(f"SELECT * FROM mobile_shop WHERE sno={sno}")
            results=mydb.fetchall()
            for row in results:
                print("Serial number=",row[0])
                print("\n")
                print("Mobile_name=", row[1])
                print("Price= ", row[2])
                print("\n")
                print("Operating_system= ", row[3])
                print("\n")
                print("Memory_storage_sim=", row[4])
                print("\n")
                print("Camera=", row[5])
                print("\n")
                print("Battery= ", row[6])
                print("\n")
                print("Processor=", row[7])
                print("\n")
                print("Display_features=", row[8])
                print("\n")
                print("Display_technology=", row[9])
                print("\n")
                print("Warranty=", row[10])
                print("\n")
                print("With_the_box=", row[11])
                print("\n")
                print("Model_no=", row[12])
                print("\n")
            cnn.commit()
            

        else:
            break

        

def cart():
    
    sql=("select mobile_name from mobile_shop")
    mydb.execute(sql)
    result=mydb.fetchall();
    sql1=("select sno from mobile_shop")
    mydb.execute(sql1)
    re=mydb.fetchall();
    sql2=("select price from mobile_shop")
    mydb.execute(sql2)
    res=mydb.fetchall();
    
    mydb.execute(f"create table FINALBILL (serialno int(50), mobilename varchar(100), price varchar(100))")
    x=input("type the serial number of the phone you want to buy")
    x1=(f"SELECT sno,mobile_name,price FROM mobile_shop WHERE sno={x}")
    mydb.execute(x1)
    r1=mydb.fetchall();
    
    y=list(r1)
    cnn.commit()
    cart1=[]
    list(cart1)
    for i in y:
        print(i)
        cart1+=i
        a=cart1[0]
        print(a)
        b=cart1[1]
        print(b)
        c=cart1[2]
        print(c)
        query="INSERT INTO finalbill (serialno,mobilename,price)\
                   VALUES ('%s', '%s', '%s')" % (a,str(b),str(c))
        mydb.execute(query)
        cnn.commit()
        cart1.clear()
        print(cart1)



#do you want to add more?
def more():
    sql=("select mobile_name from mobile_shop")
    mydb.execute(sql)
    result=mydb.fetchall();
    sql1=("select sno from mobile_shop")
    mydb.execute(sql1)
    re=mydb.fetchall();
    sql2=("select price from mobile_shop")
    mydb.execute(sql2)
    res=mydb.fetchall();
    x=input("type the serial number of the phone you want to buy")
    x1=(f"SELECT sno,mobile_name,price FROM mobile_shop WHERE sno={x}")
    mydb.execute(x1)
    r1=mydb.fetchall();
    y=list(r1)
    cnn.commit()
    cart1=[]
    list(cart1)
    for i in y:
        print(i)
        cart1+=i
        a=cart1[0]
        print(a)
        b=cart1[1]
        print(b)
        c=cart1[2]
        print(c)
        query="INSERT INTO finalbill (serialno,mobilename,price)\
                   VALUES ('%s', '%s', '%s')" % (a,str(b),str(c))
        mydb.execute(query)
        cnn.commit()
        cart1.clear()
        print(cart1)

#adding more
def add():
    for i in range(0,50):
        a=input("do you want to buy more phones?Y/N OR y/n")
        if a=="y" or a=="Y":
            more()
        else:
            print("thank you for shopping with us, we will shortly show you the bill now")
            break
    
#deleting from cart
def delete():
    sql1=("select * from finalbill order by serialno asc")
    mydb.execute(sql1)
    result=mydb.fetchall();
    for row in result:
        print("Serial number=",row[0])
        print("Mobile_name=", row[1])
        print("Price= ", row[2])
        print("\n")
    
    deldel=input("do you want to remove any item from your cart?")
    while (True):
        if deldel=='y' or deldel=='Y':
            x=input("enter the serial number of the phone you want to delete from the cart")
            sql=(f"delete from finalbill where serialno={x}")
            mydb.execute(sql)
            cnn.commit()
            e=input("do you want to delete more from the cart?")
            if e=='y' or e=='Y':
                sqlr=(f"delete from finalbill where serialno={x}")
                mydb.execute(sqlr)
                cnn.commit()
            else:
                break
        else:
            break
    sql2=("select * from finalbill order by serialno asc")
    mydb.execute(sql2)
    result2=mydb.fetchall();
    for row2 in result2:
        print("these are the phones you have bought:")
        print("Serial number=",row2[0])
        print("Mobile_name=", row2[1])
        print("Price= ", row2[2])
        print("\n")
    z=("select sum(price) from finalbill")
    mydb.execute(z)
    r1=mydb.fetchone();
    global w
    w=r1
    print(w)

#billing part in files    
def billing():
    f=open("mobile1.txt",'w')
    a=input("enter your name")
    b=input("enter your address")
    c=input("enter your mobile number")
    d=input("type mode of payment, cash on delivery or online payment?")
    g=str(w)
    f.write(a)
    f.write(b)
    f.write(c)
    f.write(g)
    f.close()
    f=open("mobile1.txt",'r')
    e=f.readline().split(',')
    print("Name:",a,"\n","address:",b,"\n","mobile number:",c,"\n",d,"\n","the total price of the items you have bought is",g)


user=input("enter a username")
password=input("enter a password")
username=[user,password]
print(username)

search()
shopping()
cart()
add()
delete()
billing()
mydb.execute("drop table finalbill")
print("thank you for shopping with us")




    




    
        
        

    

        
    





               



