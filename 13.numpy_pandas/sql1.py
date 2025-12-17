import sqlite3
con=sqlite3.connect('test.db')
cur=con.cursor()
cur.execute('''CREATE TABLE product
            (id INTEGER, name TEXT, price INTEGER, qty INTEGER)''')
cur.execute("INSERT INTO product VALUES (1,'노트북',1200000,9)")
cur.execute("INSERT INTO product VALUES (2,'데스크탑',1600000,6)")
cur.execute("INSERT INTO product VALUES (3,'마우스',20000,100)")
cur.execute("INSERT INTO product VALUES (4,'키보드',50000,65)")
cur.execute("INSERT INTO product VALUES (5,'CPU',600000,12)")

con.commit()
con.close()

