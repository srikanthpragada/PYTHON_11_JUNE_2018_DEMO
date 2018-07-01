import sqlite3
import math

con = sqlite3.connect(r"e:\classroom\python\st.db")

try:
    cur = con.cursor()
    cur.execute("select avg(fee) from courses")
    row = cur.fetchone()
    print("Average Course Fee : ", math.floor(row[0]))
except Exception as ex:
    print("Sorry! Error: ", ex)
finally:
    con.close()
