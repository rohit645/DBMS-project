import sqlite3 as sql

def insertuser(email, username, password):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO users(email, username, password) VALUES(?, ?, ?)", (email, username, password))
    con.commit()
    con.close()

def validate(username, password):
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
# def displayusers():
#     con = sql.connect("database.db")
# 	cur = con.cursor()
# 	cur.execute("SELECT email, username, password FROM users")
# 	users = cur.fetchall()
# 	con.close()
# 	return users    