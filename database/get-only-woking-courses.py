from http import client
import pymongo
client = pymongo.MongoClient()

# **get database names**
# print(client.list_database_names())
# **get collection names**
# mydb = client["training_nexus"]
# print(mydb.list_collection_names())

mydb = client["training_nexus"]
mycol = mydb["courses 3.0"]

for i in mycol.find({"coupons status" : "working"},{"course name":1,"coupon":1,"_id":0}):
    print(i)