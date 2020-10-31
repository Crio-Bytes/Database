# Introduction

### MongoDB

> MongoDB is a open-source document database and leading NoSQL database with the scalability and flexibility that you want with the querying and indexing.

### MongoDB Atlas

> MongoDB Atlas provides an easy way to host and manage your data in the cloud. MongoDB Atlas is a fully-managed cloud database.

---

> Ever wondered how to store large files like pdfs or images into databases ? If you have basic knowlegde of MySQL (A relational database), then you might know there is **blob** datatype which can be used to store pdfs. But how to do the same in MongoDB ?

> MySQL is relational database and hence it is not recommended to use for storing large amount of files, instead many professionals use MongoDB (A document-oriented NoSQL) database for it.

### Now, the solution for storing big files is using **GridFS with MongoDB**.

### **GridFS**

> GridFS is the MongoDB specification for storing and retrieving large files such as images, audio files, video files, etc. GridFS has the capability to store files even greater than its document size limit of 16MB.
> GridFS divides a file into chunks and stores each chunk(piece) of data in a separate document, each of maximum size 255K.

---

# Activities

### Activity 1: Setting up MongoDB cluster using MongoDB Atlas

[Follow the instructions in the document](https://docs.google.com/document/d/1R03KKVmihUU7nrjdTSZfwj6qLB-UvvR8OybtpjRWtFc/edit?usp=sharing)

---

### Activity 2: Import the libraries which will be required for our tasks:

-   This microbyte uses Python language for performing tasks.
-   Firstly open terminal and copy the following snippet & paste it in the terminal.

```bash
    $ pip install pymongo gridfs bson dnspython
```

1. Import MongoClient so that we can connect to a running mongod instance on our cluster.
2. Import GridFS from gridfs module so that we may put, get and delete files in MongoDB.
3. Import objectid from the bson library because we will be requiring it.
4. dnspython package is needed to make network calls to the cluster.

-   Open the command prompt and type **python** and click enter (This will turn your cmd into python shell):

```python
from pymongo import MongoClient
from gridfs import GridFS
from bson import objectid
import dns
```

---

### Activity 3: Connect to the cluster and access the database

> Now, we have imported the libraries, our task is to connect to the online cluster through our system.

**Task 1: Get the connection string to your cluster & connect to your database**

<details>
    <summary>Hint</summary>
While performing the Activity 1 above, you might have encountered with the connection string to your cluster and wondered about the use of it. This connection string is unique for every individual's cluster. Copy that connection string. Now use MongoClient to connect to it.

```python
connection_url = "mongodb+srv://CrioBytes:CrioBytes@criobytes.dyseu.mongodb.net/CrioBytes?retryWrites=true&w=majority"
conn = pymongo.MongoClient(connection_url)
# dbname will be present in your url (default db) named `test`
dbname = 'CrioBytes'
db = conn[dbname]
```

</details>
<br>

---

### Activity 4: Lets get started with interacting with our db & clear some basics

> **Task 1: Create the GridFS object**

-   **objects** ! The entire universe is made of objects !!!
-   Here, I refer object as creating the instance of GridFS class i.e. `GridFS()`.
-   `GridFS()` takes an argument which is the object (oops! again an object) of db which we created in Activity 3.

<details>
    <summary>Hint</summary>

```python
    gridfs = GridFS(db)
```

</details>

<br>

> **Task 2: Store simple string "Microbytes" in the database using gridfs**

-   Use `put()` method of gridfs instance we created to insert "Microbytes" in db
-   The `put()` method returns the object id of newly inserted object (may it be string or any file)
<details>
    <summary>Hint</summary>

```python
    obj = gridfs.put('MicroBytes')
```

</details>
<br>

**Note: This string is stored in `fs` namespace which is the default namespace used for storing data using GridFS**

> Curious about knowing what is **namespace** ?

-   A namespace is a system to have a unique name for each and every object.
-   At times, an object might be a variable or a method.
-   Lets break the keyword **namespace** as name (which means name, an unique identifier) + space(which tells us something related to scope). Here, a name might be of any method or variable and space depends upon the location from where is trying to access a variable or a method.
    <br>

---

### Activity 5: Diving deeper into GridFS

**Task 1: Create your own namespace**

-   Connect to cluster and create your own namespace while instantiating gridfs object
-   The `GridFS()` can also take another parameter which is the name of the **namespace** we wanna create.

<details>
<summary>Hint</summary>

```python
    fs = GridFS(db, "microbytes")
```

</details>

**Task 2: Insert any pdf file using gridfs**

-   Now, for inserting any file, we must have a reference pointing to that file.
-   In Python, we use `open()` function to open any file. This method returns a reference object to the file we opened.

```python
    f = open('/path_to_your_file/sample_bytes.pdf')
```

-   Use this reference object for inserting our pdf file.

<details>
<summary>Hint</summary>

```python
    file_id = fs.put(f, content_type='application/pdf', filename='sample_bytes.pdf')
    # you can provide the filename if you want to upload it with different name
```

Here, The put() method returned the file_id.

</details>
<br>

-   Now if you go to the database 'CrioBytes' in your cluster you fill find the collections named 'microbytes.files' & 'microbytes.chunks'

**Task 3: Read the uploaded file using the file_id object**

-   Can you use `get()` & `read()` method provided by `fs` object.
-   `get()` method returns a file-like-object, and to see the content, we can call `read()` method on this file-like-object.
-   Will `get()` method require some parameter associated with the file we wanna retrieve? Ofc yes ! To find the file we want, it takes in the file_id.

<details>
<summary>Hint</summary>

```python
    print(fs.get(file_id).read())
    # This will print the content of the file which has id as file_id
```

</details>
<br>

**Task 4: Let's insert txt file into MongoDB**

-   Since you have worked with inserting pdf files, this task shall not be difficult one.
-   You will perform something just like below :

```python
    f = open('/path_to_your_file/sample_bytes.pdf')
    fs.put(f, filename="sample_text.txt")
```

> What if we want to insert the file which is not present on the local system ? Can we insert some text file by inputting the data into that text file on the fly ? (dynamically) !! This might be necessary in some crucial tasks !!! So, lets see how to do so !

-   You might remember, we inserted the simple string "MicroBytes" at the start, and in subsequent task, we inserted text file. Now, the solution is simple, combine/tweak both ?

```python
    fs.put("Hello, This is a sample string", filename="new.txt")
```

<br>

**Task 5: Find a file in our database & read its contents**

-   As mentioned Task 2 of Activity 5, the files are stored in db.namespace.files collection. Use this collection to find the file stored.
-   Use `find_one()` method to find the document inside the collection.
-   Use `get()` & `read()` to read the contents of file.
<details>
    <summary>Hint</summary>

```python
    file_id = db.microbytes.files.find_one({"filename" : "sample_text.txt"},{"_id":1})
    print(fs.get(file_id['_id']).read())
    # Contents of the file `sample_text.txt` will be printed
```

</details>
<br>

**Task 6: Delete the file**

-   Now, suppose we want to delete the stored file, then use `delete()` method of `fs` object.
-   `delete()` method will also require the file_id of the file one wants to delete (Remember ! The `get()` method also needed file_id)
<details>
    <summary>Hint</summary>

```python
    fs.delete(file_id)
```

</details>
<br>
---

Hooray 🎉🎉 We have successfully setup clustes, created database,uploaded, retrieved, deleted files using GridFS file system it through our personal laptop/desktop.

# Summary

We have created a database on MongoDB Atlas and accessed it from your own laptop.

# References

1. https://docs.atlas.mongodb.com/getting-started/
2. https://www.w3schools.com/python/python_mongodb_getstarted.asp
3. https://www.tutorialspoint.com/mongodb/mongodb_gridfs.htm
4. https://psabhay.com/posts/mongodb/mongodb-gridfs-using-python/
