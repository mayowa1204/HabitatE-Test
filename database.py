import mysql.connector

def create_database():
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="Mayowa", 
            password = "oseni1234",
        )
        mycursor = db.cursor()
        mycursor.execute("CREATE DATABASE testdb") 
       
    except ConnectionError as exc:
      raise RuntimeError('Failed to connect to database') from exc
            

create_database()
  
import tables
tables.create_aunctions_table()
tables.create_results_table()

