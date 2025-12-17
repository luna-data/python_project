import sqlite3

con=sqlite3.connect('test.db')
cur=con.cursor()
cur.execute('DELETE FROM product WHERE id=2')
con.commit()

for row in cur.execute('SELECT * FROM product'):
    print(row)
con.close() 