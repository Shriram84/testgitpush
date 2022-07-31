import pymongo
client = pymongo.MongoClient("mongodb+srv://Shriram:loveline123@shriramm.7irhy.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d={
    "name": "shriram",
    'email':'shriramm@gmail.com',
    'surname' : 'Annavarapu'
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)