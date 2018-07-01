import sqlite3

con = sqlite3.connect(r"e:\classroom\python\st.db")

try:
    cur = con.cursor()
    cur.execute("insert into courses values(?,?,?,?)", (3, 'Java SE', 40, 3500))
    con.commit()
    print("Added row to COURSES table successfully!")
except Exception as ex:
    print("Sorry! Error: ", ex)
finally:
    con.close()
