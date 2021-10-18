import mysql.connector

def create_database():
 db = mysql.connector.connect(
    host="localhost",
    user="Mayowa", 
    password = "oseni1234",
)
 mycursor = db.cursor()
 mycursor.execute("CREATE DATABASE testdb") 
print("Database created successfully")

create_database()
  
import tables
tables.create_aunctions_table()
tables.create_results_table()

