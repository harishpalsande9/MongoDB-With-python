import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://harishpalsande:Zm9m2EW8QQ5Xv-R@cluster0.pbiyz7q.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)


d = {
    "name": "Harish",
    "email": "harish@gmail.com",
    "surname": "Palsande",
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)
