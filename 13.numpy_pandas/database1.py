import sqlite3
import pandas as pd

db_file="sales_data.db"

conn=sqlite3.connect(db_file)
cursor=conn.cursor()

create_table_query="""
CREATE TABLE IF NOT EXISTS sales (
    date DATE PRIMARY KEY,
    amount FLOAT
    )
    """

##이전에 실행한 sales 테이블이 존재하면 삭제
cursor.execute("DROP TABLE IF EXISTS sales")
conn.commit() 

cursor.execute(create_table_query)
conn.commit()

initial_sales_data={
    'date':['2022-01-01','2022-02-02','2022-03-03','2022-04-04','2022-05-05'],
    'amount':[1000.0,1500.0,1200.0,1800.0,900.0]
}

insert_data_query="""
INSERT INTO sales(date,amount)
VALUES(?,?)
"""

for i in range(len(initial_sales_data['date'])):
    date=initial_sales_data['date'][i]
    amount=initial_sales_data['amount'][i]
    cursor.execute(insert_data_query, (date,amount))
conn.commit()

select_query="SELECT *FROM sales"
df=pd.read_sql_query(select_query,conn)
print(df)

conn.close()