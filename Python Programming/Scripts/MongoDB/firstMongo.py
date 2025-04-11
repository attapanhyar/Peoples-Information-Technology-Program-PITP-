# pip install pymongo
# mongodb://localhost:27017/?directConnection=true


import pymongo
try:
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    print(" Successfully Connected")
    listDBs = myclient.list_database_names()
    #print(listDBs)
    # for i, db in enumerate(listDBs, start=1):
    #     print(f'{i} - {db}')
    
    mydb = myclient["PITP"] # select db
#   #print(type(mydb))
    mycollection = mydb.list_collection_names()
    # print(mycollection)
#   print(type(mycollection))
    query = input('Input Student ROllNumber')
    x = cursor = mydb.Students.find({"_id": f"{query}"})
    for i in x:
        for key, value in i.items():
            print(f'{key} : {value}')
except:
    print("Exception Caught: ")