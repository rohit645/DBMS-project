import sqlite3 as sql

def insertuser(email, username, password):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO users(email, username, password) VALUES(?, ?, ?)", (email, username, password))
    con.commit()
    con.close()

# def displayusers():
#     con = sql.connect("database.db")
# 	cur = con.cursor()
# 	cur.execute("SELECT email, username, password FROM users")
# 	users = cur.fetchall()
# 	con.close()
# 	return users    