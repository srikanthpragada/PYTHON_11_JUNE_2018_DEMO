import sqlite3

con = sqlite3.connect(r"e:\classroom\python\st.db")

try:
    cur = con.cursor()
    cur.execute("select * from courses order by id")
    for row in cur.fetchall():
        print("%3d %-30s  %3d  %5d" % (row[0], row[1], row[2], row[3]))
except Exception as ex:
    print("Sorry! Error: ", ex)
finally:
    con.close()
