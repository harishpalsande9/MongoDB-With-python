import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://harishpalsande:Zm9m2EW8QQ5Xv-R@cluster0.pbiyz7q.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

data = {
    "name": "Harish",
    "mail_id": "harish@gmail.com",
    "subject": ['Data Science', 'big Data', 'data analytics']
}


# DataBase Name
database = client['myinfo']
