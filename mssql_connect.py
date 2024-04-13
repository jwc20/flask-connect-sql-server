import dotenv
import pymssql
import os

dotenv.load_dotenv()

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

DRIVER_NAME = "SQL Server"
DATABASE_NAME = "jobs"
SERVER_NAME="WIN-ICKLJBEL43O"

conn = pymssql.connect(server=SERVER_NAME, database=DATABASE_NAME)

cursor = conn.cursor()
cursor.execute('SELECT * FROM jobs')

for row in cursor:
    print(row)

conn.close()
print("Connected to the database")
print(conn)





