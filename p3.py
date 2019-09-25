import mysql.connector;
print("establish connection with mysql now");
con = mysql.connector.connect(host="localhost",
                              database="student",
                              user="root",
                              password="");
print("connection mydb",con);

CreateTable="create table person(";
CreateTable=CreateTable+"name varchar(30) not null, age int not null )";
print(CreateTable);
cursor=con.cursor();
cursor.execute(CreateTable);
print("create table sussfully");
print("bay");
 
