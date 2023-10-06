def insert1():
    bno=int(input("enter book number:"))
    name=input("enter the name of the book:")
    author=input("enter author name:")
    genre=input("enter book genre:")
    price=float(input("enter book price:"))
    cur.execute("insert into BOOKSHELF values({},'{}','{}','{}',{})".format(bno,name,author,genre,price))
    db.commit()
def insert2():
    student=input("enter student name:")
    bname=input("enter the name of the book:")
    DOI=input("enter date of issue(yyyy/mm/dd)")
    DOR=input("enter date of return (yyyy/mm/dd)")
    cur.execute("insert into BORROWED_BOOKS values('{}','{}','{}','{}')".format(student,bname,DOI,DOR))
    db.commit()
def insert3():
    student=input("enter student name:")
    book=input("enter borrowed book name:")
    days=input("enter the number of days overdue:")
    cur.execute("insert into DEFAULTERS values('{}','{}',{})".format(student,book,days))
    db.commit()
def display():
    print("Existing tables: BOOKSHELF,BORROWED_BOOKS,DEFAULTERS")
    table=input("enter table name to display:")
    if table=="BOOKSHELF":
        cur.execute("select * from BOOKSHELF")
        for i in cur:
            print(i)
    elif table=="BORROWED_BOOKS":
        cur.execute("select * from BORROWED_BOOKS")
        for i in cur:
            print(i)
    elif table=="DEFAULTERS":
        cur.execute("select * from DEFAULTERS")
        for i in cur:
            print(i)
    else:
        print("incorrect table name")
def ORDER_1():
    cur.execute("select * from BORROWED_BOOKS ORDER BY Date_of_Issue")
    for i in cur:
        print(i)
def ORDER_2():
    cur.execute("select * from BORROWED_BOOKS ORDER BY Date_of_Return") 
    for i in cur:
        print(i)
def ORDER_3():
    cur.execute("select * from DEFAULTERS ORDER BY DAYS_OVERDUE desc")
    for i in cur:
        print(i)
def update():
    student=input("enter student name:")
    cur.execute("select STUDENT_NAME from BORROWED_BOOKS")
    l1=list(cur)
    if (student,) in l1:
        dor=input("enter new date of return (yyyy/mm/dd):")
        cur.execute("update BORROWED_BOOKS set Date_of_Return='{}' where STUDENT_NAME='{}'".format(dor,student))
        db.commit()
        print("record updated successfully")
    else:
        print("student record not found")
def alter_table():
    student=input("enter student name:")
    cur.execute("select STUDENT_NAME from BORROWED_BOOKS")
    l1=list(cur)
    if (student,) in l1:
        book=input("enter new book name:")
        cur.execute("update BORROWED_BOOKS set BOOK_NAME='{}' where STUDENT_NAME='{}'".format(book,student))
        db.commit()
        print("record updated sucessfully")
    else:
        print("student record does not exist")
def available_books():
    cur.execute("select BOOK_NAME from BOOKSHELF")
    list1=list(cur)
    cur.execute("select BOOK_NAME from BORROWED_BOOKS")        
    list2=list(cur)
    for i in list1:
        if i not in list2:
            print(i)
def delete():
    table=input("enter table name for records to be deleted:")
    if table=="BOOKSHELF":
        book=input("enter book name to be deleted:")
        cur.execute("select BOOK_NAME from BOOKSHELF")
        l1=list(cur)
        if (book,) in l1:
            cur.execute("delete from BOOKSHELF where BOOK_NAME='{}'".format(book))
            print("record deleted..")
        else:
            print("record does not exist")
    elif table=="BORROWED_BOOKS":
        student=input("enter student name to delete record:")
        cur.execute("select STUDENT_NAME from BORROWED_BOOKS")
        l2=list(cur)
        if (student,) in l2:
            cur.execute("delete from BORROWED_BOOKS where STUDENT_NAME='{}'".format(student))
            print("record deleted..")
        else:
            print("record does not exist")
    elif table=="DEFAULTERS":
        student=input("enter student name to delete record:")
        cur.execute("select STUDENT_NAME from DEFAULTERS")
        l3=list(cur)
        if (student,) in l3:
            cur.execute("delete from DEFAULTERS where STUDENT_NAME='{}'".format(student))
            print("record deleted..")
        else:
            print("record does not exist")
    else:
        print("invalid table name..")          
import mysql.connector,datetime
db=mysql.connector.connect(host="localhost",user="root",password="root",database="library")
cur=db.cursor()
print(datetime.datetime.now())
try:
    q1="""create table BOOKSHELF(BNo integer NOT NULL,BOOK_NAME varchar(30) NOT NULL PRIMARY KEY,
AUTHOR_NAME varchar(15),GENRE varchar(10),PRICE decimal)"""
    cur.execute(q1)
    q2="""create table BORROWED_BOOKS(STUDENT_NAME varchar(20) NOT NULL PRIMARY KEY,
BOOK_NAME varchar(30) NOT NULL,Date_of_Issue varchar(10),Date_of_return varchar(10))"""
    cur.execute(q2)
    q3="""create table DEFAULTERS(STUDENT_NAME varchar(20) NOT NULL PRIMARY KEY,
BOOK_NAME varchar(30),DAYS_OVERDUE integer)"""
    cur.execute(q3)
except:
    pass    
out="Y"   
while out not in "Nn":
    ch=int(input("""1:To enter books in BOOKSHELF
2:To enter borrowed books from BOOKSHELF 
3:To enter defaulters record
4:To display tables
5:To view borrowed books in sequence of date of issue
6:To view borrowed books in sequence of date of return
7:To view defaulters in decreasing order of number of days overdue
8:To update student's date of return of borrowed books
9:To alter names of books borrowed by student
10:To view books currently available in bookshelf 
11:To delete records from a table 
Enter response:"""))
    if ch==1:
        insert1()
    elif ch==2:
        insert2()
    elif ch==3:
        insert3()
    elif ch==4:
        display()
    elif ch==5:
        ORDER_1()
    elif ch==6:
        ORDER_2()
    elif ch==7:
        ORDER_3()
    elif ch==8:
        update()
    elif ch==9:
        alter_table()
    elif ch==10:
        available_books()
    elif ch==11:
        delete()
    else:
        print("invalid response...")
    out=input("do you want to continue?:(Y/N)")    
    
