import dotenv
# import pypyodbc as odbc
import pymssql
import os


# Load the environment variables
dotenv.load_dotenv()

# Get the environment variables
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
# SERVER_NAME = os.getenv("SERVER_NAME")


# Connect to the database
DRIVER_NAME = "SQL Server"
# SERVER_NAME = "localhost"
DATABASE_NAME = "jobs"
SERVER_NAME="WIN-ICKLJBEL43O"

    # uid={USERNAME};
    # pwd={PASSWORD};


# connection_string = f"""
#     DRIVER={{{DRIVER_NAME}}};
#     SERVER={SERVER_NAME};
#     DATABASE={DATABASE_NAME};
#     Trusted_Connection=yes
# """

# connection = odbc.connect(connection_string)

# print("Connected to the database")
# print(connection)

conn = pymssql.connect(server=SERVER_NAME, database=DATABASE_NAME)

cursor = conn.cursor()
cursor.execute('SELECT * FROM jobs')
for row in cursor:
    print(row)
conn.close()
print("Connected to the database")
print(conn)





