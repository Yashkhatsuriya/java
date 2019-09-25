import mysql.connector;
print("establish connection with mysql now");
con = mysql.connector.connect(host="localhost",
                              database="employee",
                              user="root",
                              password="");
print("connection mydb",con);

CreateTable="create table emp11(";
CreateTable=CreateTable+"empno int not null,empname varchar(15) not null,gender boolean not null,bdate date not null,joindate date not null,basicsalary decimal not null)";
print(CreateTable);
cursor=con.cursor();
cursor.execute(CreateTable);
print("create table sussfully");
print("bay");
