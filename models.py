import sqlite3 as sql

def get_db():
    con = sql.connect("database.db")
    return con

def insertstudent(rollno, email, password):
    con = get_db()
    cur = con.cursor()
    cur.execute("INSERT INTO student(ROLLNO, EMAIL, PASSWORD) VALUES(?, ?, ?)", (rollno, email, password))
    con.commit()
    cur.close()
    con.close()

def validatestudent(username, password):
    con = sql.connect("database.db")
    print('inside validate')
    check = False
    with con:
        cur = con.cursor()
        cur.execute("select * from users")
        rows = cur.fetchall()
        for row in rows:
            dbuser = row[2]
            dbpass = row[3]
            if (dbuser==username):
                if (password == dbpass):
                    check = True
    return check
def check_duplicate_student(rollno):
    con = get_db()
    print('inside checking duplicate values!')
    check = False
    with con:
        cur = con.cursor()
        cur.execute("select ROLLNO from student")
        rows = cur.fetchall()
        for row in rows:
            dbrno = row[0]
            if (dbrno==rollno):
                check = True
    # cur.close()
    print(check)
    return check
    

# def displayusers():
#     con = sql.connect("database.db")
# 	cur = con.cursor()
# 	cur.execute("SELECT email, username, password FROM users")
# 	users = cur.fetchall()
# 	con.close()
# 	return users    