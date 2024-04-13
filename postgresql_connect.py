from dotenv import load_dotenv
import psycopg2
import os

load_dotenv()

DATABASE = os.getenv('DATABASE')
DATABASE_USERNAME = os.getenv('DATABASE_USERNAME')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')

    
try:
    conn = psycopg2.connect(
    database=DATABASE,
    user=DATABASE_USERNAME,
    password=DATABASE_PASSWORD)

    print(conn)
    cur = conn.cursor()

    cur.execute('select * from clients')
    rows = cur.fetchall()
    print(rows)

except:
    print('Error')

