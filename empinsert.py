import mysql.connector;
print("establish connection with mysql now");
con = mysql.connector.connect(host="localhost",
                              database="employee",
                              user="root",
                              password="");
print("connection mydb",con);

eno=input("enter employee no ");
nm=input("enter name ");
gen=input("enter gender ");
if(gen == "male" or gen=="Male"):
    gender = "1";
elif(gen == "female" or gen=="Female"):
    gender = "0";
    
bdate=input("enter birthdate ");
jdate=input("enter joindate ");
bs=input("enter basic salary ");

Insert= " Insert into emp11 values(";
Insert=Insert+eno+",";
Insert=Insert+"'"+nm+"',";
Insert=Insert+"'"+gender+"',";
Insert=Insert+bdate+",";
Insert=Insert+jdate+",";
Insert=Insert+bs+ ")";




cursor=con.cursor();
result=cursor.execute(Insert);
con.commit();
print("sussesfullY inserted");

