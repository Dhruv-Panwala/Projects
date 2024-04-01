import mysql.connector

mydb = mysql.connector.connect(user = 'root', password = 'mysql', host = 'localhost', database='gymmanagement')

if(mydb.is_connected()):
    print("Connection Established")
else:
    print("Not Connected")
cur = mydb.cursor()

# cur.execute("CREATE TABLE CUST_DETAILS(ID int(4) AUTO_INCREMENT,NAME VARCHAR(50) NOT NULL, MOB_NUMBER int(10) NOT NULL, SUBS_END DATE NOT NULL, JOIN_DATE DATE NOT NULL, PRIMARY KEY(ID,NAME))")

# cur.execute("CREATE TABLE CUST_PHY_DETAILS(ID INT(4), NAME VARCHAR(50), HEIGHT FLOAT NOT NULL, CURR_WEIGHT FLOAT NOT NULL,BMI FLOAT NOT NULL, TARGET_WEIGHT FLOAT NOT NULL,FOREIGN KEY(ID,NAME) REFERENCES CUST_DETAILS(ID,NAME))")

# cur.execute("CREATE TABLE CUST_LOGIN(ID INT(4), NAME VARCHAR(50), DATE DATE NOT NULL,ENTER_TIME TIME NOT NULL, EXIT_TIME TIME NOT NULL, ENTER_WEIGHT FLOAT NOT NULL, EXIT_WEIGHT FLOAT NOT NULL,FOREIGN KEY(ID,NAME) REFERENCES CUST_DETAILS(ID,NAME))")
cur.execute("ALTER TABLE CUST_DETAILS MODIFY PASSWORD VARCHAR(20) Not NULL")
# cur.execute("ALTER TABLE CUST_LOGIN MODIFY EXIT_WEIGHT FLOAT NULL")
# cur.execute("Alter Table cust_details add column Gender varchar(1) NOT NULL")
mydb.commit()
