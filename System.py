# Weight in kilograms = 2.2 x BMI + (3.5 x BMI) x (Height in meters minus 1.5)
# BMI = weight/(height)^2
import mysql.connector
import datetime

mydb = mysql.connector.connect(user = 'root', password = 'mysql', host = 'localhost', database='gymmanagement')

if(mydb.is_connected()):
    print("Connection Established")
else:
    print("Not Connected")
cur = mydb.cursor()

class Err(Exception):
    pass

class NoChoice(Err):
    pass
class IncorrectPassword(Err):
    pass
class NameDoesNotExist(Err):
    pass
class ScriptionEnded(Err):
    pass

try:
    print("Sign UP------------------>1")
    print("Sign IN------------------>2")
    print("Sign out----------------->3")
    print("Subscription Renewal----->4")
    choice=int(input("Enter Your Choise:"))
    if(choice==1):
        name=input("Enter Full Name:")
        number=int(input("Enter Mobile number"))
        from datetime import datetime
        joining= datetime.today()
        password=input("Enter Password:")
        gender=input("Enter Gender M/F/O:")
        cur.execute("SELECT DATE_ADD(SYSDATE(), INTERVAL 1 YEAR) FROM DUAL")
        subscription=cur.fetchone()
        que="INSERT INTO CUST_DETAILS (ID,NAME,MOB_NUMBER,SUBS_END,JOIN_DATE,PASSWORD,Gender)VALUES(%s,%s,%s,%s,%s,%s,%s)"
        val=(2,name,number,subscription[0],joining,password,gender)
        cur.execute(que,val)

        height=float(input("Enter Height in meters:"))
        weight=float(input("Enter weight in kg:"))
        BMI=weight/(height**2)
        # 2.2 x BMI + (3.5 x BMI) x (Height in meters minus 1.5)
        target=(2.2 *BMI)+((3.5*BMI)*(height-1.5))
        que="INSERT INTO CUST_PHY_DETAILS VALUES(%s,%s,%s,%s,%s,%s)"
        val1=(2,name,height,weight,BMI,target)
        cur.execute(que,val1)
        mydb.commit()
    elif(choice==2):
        name=input("Enter Name:")
        cur.execute("Select PASSWORD,SUBS_END from cust_details where name=%s",(name,))
        check=cur.fetchall()
        date= datetime.date.today()
        print(check)
        if(date<check[0][1]):
            password=input("Enter Password:")
            if(password==check[0][0]):  
                from datetime import datetime
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                current_weight=float(input("Enter Weight:"))
                que="INSERT INTO CUST_LOGIN (NAME,DATE,ENTER_TIME,ENTER_WEIGHT) VALUES (%s,%s,%s,%s)"
                val=(name,date,current_time,current_weight)
                cur.execute(que,val)
                mydb.commit()
            else:
                raise IncorrectPassword
        else:
            raise ScriptionEnded
    elif(choice==3):
        name=input("Enter Name:")
        password=input("Enter Password:")
        cur.execute("Select password from cust_details where name=%s",(name,))
        check=cur.fetchone()
        if(password==check[0]):
            date= datetime.date.today()
            from datetime import datetime
            now = datetime.now()
            exit_time = now.strftime("%H:%M:%S")
            exit_weight=float(input("Enter Weight:"))
            que="UPDATE CUST_LOGIN SET EXIT_TIME=%s, EXIT_WEIGHT=%s WHERE NAME=%s AND DATE=%s"
            val=(exit_time,exit_weight,name,date)
            cur.execute(que,val)
            que="UPDATE CUST_PHY_DETAILS SET CURR_WEIGHT=%s where NAME=%s"
            val1=(exit_weight,name)
            cur.execute(que,val1)
            mydb.commit()
        else:
            raise IncorrectPassword
    elif (choice==4):
        name=input("Enter Name:")
        password=input("Enter Password:")
        cur.execute("Select password from cust_details where name=%s",(name,))
        check=cur.fetchone()
        if(password==check[0]):
            cur.execute("SELECT DATE_ADD(curdate(), INTERVAL 1 YEAR) FROM DUAL")
            subscription=cur.fetchone()
            print(subscription[0])
            cur.execute("UPDATE CUST_DETAILS SET SUBS_END='%s' where NAME='%s'",(subscription[0],name))
            mydb.commit()
        else:
            raise IncorrectPassword
    else:
        raise NoChoice
except NoChoice:
    print("No Such Choice Available")
    raise
except IncorrectPassword:
    print("Password Does not match")
    raise
except NameDoesNotExist:
    print("Name Not Found")
    raise
except ScriptionEnded:
    print("Your Subscription is ended.Please renew your subscription")
