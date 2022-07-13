import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database = "csgotradeup"
)
mycursor = mydb.cursor()

def database_size(database_name, table_name):
    query = "SELECT  table_name AS `Table`, \
    round(((data_length + index_length) \
    / 1024 / 1024), 2) `Size in MB` \
    FROM information_schema.TABLES \
    WHERE table_schema = %s AND \
    table_name = %s;"
    mycursor.execute(query, (database_name, table_name))
    data = mycursor.fetchall()
    for item in data:
        return item[-1],data