import mysql.connector;
print("establish connection with mysql now");
con = mysql.connector.connect(host="localhost",
                              database="student",
                              user="root",
                              password="");
print("connection mydb",con);
print("bay...");
