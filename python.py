import mysql.connector
from tabulate import tabulate
con=mysql.connector.connect(host='localhost',database='mydb',user='root',password='Abiarunela@42')
if con:print('connect')
def insert(e_name,job_des):
    res=con.cursor()
    sql='insert into employee(e_name,job_des) values (%s,%s)'
    user=(e_name,job_des)
    res.execute(sql,user)
    con.commit()
    print('Insert the data successfully')


def update(e_name,job_des,id):
    res=con.cursor()
    sql='update employee set e_name=%s , job_des=%s where id=%s'
    user=(e_name,job_des,id)
    res.execute(sql,user)
    con.commit()
    print('Update the data successfully')


def show():
    res=con.cursor()
    sql='select * from employee'
    res.execute(sql)
    result=res.fetchall()
    print(tabulate(result,headers=['Id','Employee Name','Profession']))
def delete(id):
    res=con.cursor()
    sql='delete from employee where id=%s'
    user = (id,)
    res.execute(sql,user)
    con.commit()
    print('Delete the data successfully')
while True:
    print('1.Insert the datas')
    print('2.Update the datas')
    print('3.Display table')
    print('4.Delete the data')
    print('5.Exit')
    choice=int(input('Enter your choice :'))
    if choice==1:
        e_name=input('Enter a name :')
        job_des=input('Enter your profession :')
        insert(e_name,job_des)
    elif choice==2:
        id=input('update the id :')
        e_name=input('update the name :')
        job_des=input('update the profession :')
        update(e_name,job_des,id)
    elif choice==3:
        show()
    elif choice==4:
        id=input('Delete a id :')
        delete(id)
    elif choice==5:
        quit()
    else:
        print('Invalid Choice , please try again!')
