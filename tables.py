import mysql.connector
from datetime import datetime

db = mysql.connector.connect(
    host="localhost",
    user="Mayowa", 
    password = "oseni1234",
    database = "testdb"
)
mycursor = db.cursor()

def create_aunctions_table ():
  mycursor.execute("CREATE TABLE AUNCTIONS(resource_id varchar(255) NOT NULL, links_start varchar(255) NOT NULL, links_next varchar(255) NOT NULL, aunction_date datetime NOT NULL,  total int NOT NULL ,  id int PRIMARY KEY NOT NULL AUTO_INCREMENT )" )
  db.commit()


def create_results_table ():
    mycursor.execute("CREATE TABLE RESULTS(api_id int NOT NULL, company varchar(255) NOT NULL, unit_name varchar(50) NOT NULL,efa_date datetime NOT NULL, delivery_start datetime NOT NULL , delivery_end datetime NOT NULL, efa int NOT NULL, service varchar(50), cleared_volume int NOT NULL, clearing_price int NOT NULL, technology_type varchar(50) NOT NULL, cancelled varchar(50) NOT NULL, aunctionId int NOT NULL, id int PRIMARY KEY NOT NULL AUTO_INCREMENT )" )
    db.commit()

async def create_aunction(aunction, aunction_date):
    print(aunction)
    links = aunction["_links"]
    links_start = links["start"]
    links_next = links["next"]
    print (aunction["include_total"])
    query = "INSERT INTO AUNCTIONS(resource_id,links_start, links_next,  total, aunction_date) Values(%s, %s,%s, %s,%s)"
    mycursor.execute( query, (aunction["resource_id"], links_start, links_next, aunction["total"], aunction_date))
    db.commit()
    last_id = mycursor.lastrowid
    return last_id
   
async def create_result(result,  aunction_id):
    api_id = result['_id']
    company= result['Company']
    unit_name= result['Unit Name']
    efa_date = result['EFA Date']
    delivery_start =result['Delivery Start'] 
    delivery_end = result['Delivery End'] 
    efa = result["EFA"] 
    service = result["Service"]
    cleared_volume = result["Cleared Volume"]
    clearing_price = result["Clearing Price"]
    technology_type =result["Technology Type"]
    cancelled = result["Cancelled"]
    query = "INSERT INTO RESULTS(api_id,company, unit_name, efa_date,delivery_start, delivery_end, efa, service, cleared_volume, clearing_price, technology_type, cancelled, aunctionId) Values(%s, %s, %s,%s, %s, %s, %s, %s, %s,%s, %s, %s,%s)"
    mycursor.execute( query, ( api_id, company, unit_name,efa_date,delivery_start, delivery_end, efa , service, cleared_volume,clearing_price ,technology_type, cancelled, aunction_id))
    db.commit()
    last_id = mycursor.lastrowid
    print(last_id)
    return last_id


async def get_results():
     mycursor.execute("SELECT * FROM Aunctions")
     for x in mycursor:
      return x
     






 
