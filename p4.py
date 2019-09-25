import mysql.connector;
print("establish connection with mysql now");
con = mysql.connector.connect(host="localhost",
                              database="student",
                              user="root",
                              password="");
print("connection mydb",con);

nm=input("enter name");
ag=input("enter age");
#bd=input("enter date");

Insert= " Insert into person values(";
Insert=Insert+"'"+nm+"',";
Insert=Insert+ag+")";
#Insert=Insert+"'"+bd+" ' )";

cursor=con.cursor();
result=cursor.execute(Insert);
con.commit();
print("sussesfullY inserted");

