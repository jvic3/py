import sqlite3


conn = sqlite3.connect('example.db')
print("Opened database successfully")

conn.execute("INSERT INTO EMPLOYEES VALUES (1, 'FAITH',30,567000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (2, 'FAITH',28,590000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (3, 'FAITH',25,345000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (4, 'FAITH',40,675000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (5, 'FAITH',60,250000.00)")

conn.commit()
print("Records inserted successfully")
conn.close()