import mysql.connector;
print("establish connection with mysql now");
con = mysql.connector.connect(host="localhost",
                              database="student",
                              user="root",
                              password="");
print("connection mydb",con);

CreateTable="create table stude1(";
CreateTable=CreateTable+"rollno int not null, name varchar(20) not null,semestor int not null,gender boolean not null,pythonmark int not null,phpmark int not null,javamark int not null,total int ,percentage int ,gread varchar(5))";
print(CreateTable);
cursor=con.cursor();
cursor.execute(CreateTable);
print("create table sussfully");
print("bay");
