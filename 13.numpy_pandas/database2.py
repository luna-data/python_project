import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def connect_db(db_file):
    conn=sqlite3.connect(db_file)
    return conn

def get_monthly_sales(conn):
    query="""
    SELECT strftime('%Y-%m', date) AS month,
           SUM(amount) AS total_sales
    FROM sales
    GROUP BY month
    ORDER BY month
    """

    df=pd.read_sql_query(query,conn)
    return df

def visualize_monthly_sales(df):
    plt.figure(figsize=(10,6))
    plt.plot(df['month'], df['total_sales'], marker='o',linestyle="-")
    plt.title('Monthly Sales Data Visualization')
    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

db_file="sales_data.db"
conn=connect_db(db_file)
monthly_sales_df=get_monthly_sales(conn)

visualize_monthly_sales(monthly_sales_df)

conn.close()
