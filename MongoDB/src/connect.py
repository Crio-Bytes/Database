import pymongo
import dns

db_name = "CrioBytes"
connection_url = "mongodb+srv://CrioBytes:<password>@criobytes.dyseu.mongodb.net/"+db_name+"?retryWrites=true&w=majority"
collection_name = "users"
# This url will be different for everyone.
# Update the password your user's password (You will have to create one new user if not available).
conn = pymongo.MongoClient(connection_url)
db = conn[db_name]
col = db[collection_name]

# data to be inserted in database db & in collection col
user = {"name": "Jackie", "gender": "Male" }

# insert_one is used to insert single document 
ins_doc = col.insert_one(user)

# print the document id of the newly inserted document
print("The id of newly inserted document is: ", ins_doc.inserted_id)

new_user = {"name": "Julia" , "gender": "Female"}
ins_doc = col.insert_one(new_user)
# print the document id of the newly inserted document
print("The id of newly inserted document is: ", ins_doc.inserted_id)

for c in col.find(): 
    print(c)
