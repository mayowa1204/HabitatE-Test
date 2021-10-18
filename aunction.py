import json
import requests 
import tables
import asyncio


async def get_aunction_data():
    response = requests.get("https://data.nationalgrideso.com/api/3/action/datastore_search?resource_id=ddc4afde-d2bd-424d-891c-56ad49c13d1a")
    print(response.json())
    res = json.loads(response.text)
    result = res['result']
    records =  result['records']
    end_date = records[0]["Delivery End"]
    return {"aunction_date":end_date, "records":records, "result":result}

async def store_result_data(result, end_date):
    aunction_id = await tables.create_aunction(result, end_date)
    print(aunction_id)
    return aunction_id

async def store_aunction_data(records, aunction_id):
    for x in records:
        answer = await tables.create_result(x, aunction_id)
        print(answer)

async def get_and_store_data():
   data =  await get_aunction_data()
   result = data["result"]
   aunction_date = data["aunction_date"]
   records = data["records"]
   aunction_id = await store_result_data(result, aunction_date)
   await store_aunction_data(records, aunction_id)
   aunction = await tables.get_results()
   print(aunction) 
   return aunction


asyncio.run(get_and_store_data())