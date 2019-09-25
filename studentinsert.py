import mysql.connector;
print("establish connection with mysql now");
con = mysql.connector.connect(host="localhost",
                              database="student",
                              user="root",
                              password="");
print("connection mydb",con);

rn=input("enter rollno ");
nm=input("enter name ");
sem=input("enter semestor ");
gen=input("enter gender ");
if(gen == "male" or gen=="Male"):
    gender = "1";
elif(gen == "female" or gen=="Female"):
    gender = "0";
    
pym=input("enter python mark ");
phpm=input("enter php mark ");
jm=input("enter java mark ");

Insert= " Insert into stud values(";
Insert=Insert+rn+",";
Insert=Insert+"'"+nm+"',";
Insert=Insert+sem+",";
Insert=Insert+"'"+gender+"',";
Insert=Insert+pym+",";
Insert=Insert+phpm+",";
Insert=Insert+jm+ ")";




cursor=con.cursor();
result=cursor.execute(Insert);
con.commit();
print("sussesfullY inserted");

