import json
import requests 
import tables
import asyncio

## getting the aunction data
async def get_aunction_data():
    try:
        response = requests.get("https://data.nationalgrideso.com/api/3/action/datastore_search?resource_id=ddc4afde-d2bd-424d-891c-56ad49c13d1a")
        res = json.loads(response.text)
        result = res['result']
        records =  result['records']
        end_date = records[0]["Delivery End"]
        return {"aunction_date":end_date, "records":records, "result":result}
    except RuntimeError:
             raise RuntimeError("failed retrieve data")
        
# storing the aunction metadata
async def store_result_data(result, end_date):
    try:
        aunction_id = await tables.create_aunction(result, end_date)
        return aunction_id
    except Exception: 
             print("failed to create new aunction")
        
#storing the aunction records 
async def store_aunction_data(records, aunction_id):
    try:
        for x in records:
         await tables.create_result(x, aunction_id)
         
    except Exception:
         print("failed to store aunction results")
        

async def get_and_store_data():
    try:
        data =  await get_aunction_data()
        result = data["result"]
        aunction_date = data["aunction_date"]
        records = data["records"]
        aunction_id = await store_result_data(result, aunction_date)
        await store_aunction_data(records, aunction_id)
        aunction = await tables.get_results() 
        return aunction
    except Exception:
         print ("failed to create aunctions table")
        


asyncio.run(get_and_store_data())

