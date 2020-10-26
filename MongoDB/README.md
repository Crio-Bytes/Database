# Introduction

### MongoDB

> MongoDB is a open-source document database and leading NoSQL database with the scalability and flexibility that you want with the querying and indexing.

### MongoDB Atlas

> MongoDB Atlas provides an easy way to host and manage your data in the cloud. MongoDB Atlas is a fully-managed cloud database.

---

# Prerequisites

No background knowledge is required for this tutorial, just simply follow the activities given below.

---

# Activities

### Activity 1: Create or login into MongoDB Atlas account

-   Either Register on: https://account.mongodb.com/account/register

    <img src="images/register.png">

    **(OR)**

    Login at: https://account.mongodb.com/account/login

    <img src="images/login.png"/>

-   You will land on the following dashboard page:

    <img src="images/dashboard.png"/>

### Activity 2: Create a new cluster for your database

-   Click on Create Cluster on dashboard page and choose the type of cluster plan

    <img src="images/dashboard.png"/>

-   Choose on Cloud Provider & Cloud region

    <img src="images/createCluster1.png"/>

-   Choose your cluster settings & name your cluster

    <img src="images/createCluster2.png"/>

-   Now, click "Create Cluster" and it will take a few minutes to setup your cluster on cloud

    <img src="images/createCluster3.png"/>

### Activity 3: Add Connection and your IP address to the list to access the cluster

-   Click on "Connnect" for conncection setup

      <img src="images/setup0.jpg"/>

-   Here, this tutorial uses connect using by using MongoDB's native drivers (Option2)

      <img src="images/setup1.jpg"/>

-   Here, choose the driver of your choice e.g. Python, Nodejs and choose the version of lanugage you are using.

      <img src="images/setup2.jpg"/>

-   For adding the IP address click on "Network Access" and all your IP address over there(This is done for secure access to cluster).

-   If you want the cluster to be accessible from everywhere, then just ensure whether there exists an entry of 0.0.0.0 in the list.

-   Now, create a python file and insert the following snippet

**Note: Copy the driver code example of your created cluster, as the connection url is different for each cluster**

```python
import pymongo

connection_url = "mongodb+srv://Girish:<password>@criobytes.dyseu.mongodb.net/<dbname>?retryWrites=true&w=majority"

# This url will be different for everyone.
# Update the <password> with your user's password (You will have to create one new user if not available).
# Replace <dbname> with the name of database of your choice.

client = pymongo.MongoClient(connection_url)
db = client.test
```

### Activity 4: Install the native driver library to connect to your MongoDB Cluster

-   This tutorial uses Python language for demonstration.
-   Firstly open terminal and copy the following snippet & paste it in the terminal.

```bash
    $ pip install pymongo
```

### Activity 5: Run the python file & watch the results

-   Python code snippet for accessing & performing read/writes on the database in your cluster

```python

import pymongo
# pip install dnspython (This library is needed to make network calls to the cluster)
import dns

db_name = "CrioBytes"
connection_url = "mongodb+srv://CrioBytes:CrioBytes@criobytes.dyseu.mongodb.net/"+db_name+"?retryWrites=true&w=majority"
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
```

-   The output of above code:

    <img src="./images/output1.png">

-   Now, go to the cluster on atlas and click collections, one will find the newly inserted data being updated there.

      <img src="./images/output2.png">

<br>
Hooray 🎉🎉 We have successfully setup clusters, created database and acccessed it through our personal laptop/desktop.

# Summary

We have created a database on MongoDB Atlas and accessed it from your own laptop.

# References

1. https://docs.atlas.mongodb.com/getting-started/
2. https://www.w3schools.com/python/python_mongodb_getstarted.asp
