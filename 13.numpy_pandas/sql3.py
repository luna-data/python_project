import sqlite3
con=sqlite3.connect('test.db')
cur=con.cursor()
cur.execute("UPDATE product SET price = 2000000 WHERE id =1")
con.commit()

for row in cur.execute('SELECT * FROM product'):
    print(row)

con.close()