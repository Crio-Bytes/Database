# Welcome to  Basics of MySQL
***

## INTRODUCTION

## What is MySQL?
**MySQL is a standard language for storing, manipulating and retrieving data. It is a relational database management system software.**

## What you will be learning in this Micro-Byte?
It is really important to get started with the basics and understand the concepts and commands to manipulate data stored in tables in MySQL. MySQL is of primary importance. No matter which field you pursue ahead in your career, be it data science, cloud computing, software development or any related discipline, you will have to know about the fundamentals of DBMS i.e- MySQL. 

### Pre-requisites

**MySQL Editor**
I would be using MySQL command line client 8.0. 
You can download from https://dev.mysql.com/doc/refman/8.0/en/mysql.html .
After doing the setup. You can access by entering your admin password.The console should look 

<details>
  <summary>Terminal</summary>
 
 ![first](https://github.com/happycoder0011/Database/blob/happycoder0011/basics_of_MySQl/add/Basics%20of%20MySQL/Images/Screenshot%20(83).png)
</details>

## Activity - 0
### Task -1 
**Create Database**
The tables or the relations are held inside a database. So firstly you will have to create a data base.
- Create Database:

```sh
create database database_name;
```

![second](https://github.com/happycoder0011/Database/blob/happycoder0011/basics_of_MySQl/add/Basics%20of%20MySQL/Images/Screenshot%20(84).png)


> **Note:** MySQL is not case sensitive.
- To view all the databases you have in your system:
```sh
show databases;
```

![third](https://github.com/happycoder0011/Database/blob/happycoder0011/basics_of_MySQl/add/Basics%20of%20MySQL/Images/Screenshot%20(85).png)

you will get a list of databases.

- To use any of the databases and create tables inside it:
```sh
use database_name;
```
You will get a message - **" Database Changed"**.
Now you can start creating tables inside your database.
### Task-2
**Create Table**
Now, You need to know that in a table there are two major components - 
- **Data** - It is the values of different entities that you store in a table.For eg- In a students table, you will have data of different students such as rohan,nikhil etc.Their marks, class and other features in different rows.
- **Metadata** - Metadata is generally known as data about the data. In simple terms, you can understand it as data has certain properties when getting stored.
Lets take an example,
In the students table, you may have columns such as student ID, name, course, marks etc. You can set the datatypes of your data, which is again a metadata as it tells about your data. The datatypes can be
    - Numeric Datatype ( Int, float)
    - String Datatype  (char, varchar)
    - date and time
    - Spatial Datatype
    - Json datatype
    
Lets say, student ID can be numeric or alpha numeric. The marks can be float or int and so on.  
Table in MySQL is created by mentioning the names of columns and metadata. For now lets just use the datatypes as metadata. We will be discussing more of it furthur. 
- To create a student table with columns datatype:

<center>

| Columns  | Datatype|
| --- | ---|
|Student_ID | Varchar(20) |
|First_Name | Varchar(40) |
|Last_Name | Varchar(40) |
|Course_ID | Int |
|Course_Name | Varchar(40) |
|Admission_Date | date |
</center>

```sh
create table table_name(Column_1 datatype_1, 
                        Column_2 datatype_2,
                        Column_3 datatype_3,
                        Column_4 datatype_4,);
```

<details>
  <summary>Hint</summary>
  
  ```javascript
   create table student(Student_ID varchar(40), 
                     First_Name varchar(40), 
                     Last_Name varchar(40), 
                     Course_ID int, 
                     Course_Name varchar(40), 
                     Admission_date date);
  ```
</details>


- To check your table has been created:

```sh
describe table_name;
```
![fifth](https://github.com/happycoder0011/Database/blob/happycoder0011/basics_of_MySQl/add/Basics%20of%20MySQL/Images/Screenshot%20(87).png)

- To view the list of all the tables in your database:
```sh
show tables;
```
### Task-3
**Insert values in table**
The table has been created. Now, you can insert your data in your table.


- To insert data in the table:
<details><summary>Hint</summary>
```sh
insert into student values("AC101","ROHAN","KUMAR",1,"Accountancy","2020-07-02");
```
</details>


- To insert values in selected columns:


<details>
  <summary>Hint</summary>
  
  ```javascript
   insert into student values("AC101","ROHAN","KUMAR",1,"Accountancy","2020-07-02");
  ```
</details>


To insert values in selected columns


```sh
 INSERT INTO table_name(column_1,column_2) VALUES("value_1","value_2");
```
<details>
  <summary>Hint</summary>
  
  ```javascript
   INSERT INTO STUDENT(First_name,Last_Name) VALUES("Karan","kashyap");
  ```
</details>

**View table**
- To check and view your table:

```sh
select * from table_name;
```
> **Note:** "*" implies display all the columns.

- To view selective columns:
```sh
select column_1,column_2 from table_name;
```

<details>
  <summary>Hint</summary>
  
  ```javascript
  select student_id,first_name from student;
  ```
</details>

## Activity - 1

You learnt to create and insert values in your table. You can think of situations where you may wish to add a column or alter(change) some value.We will learn about those commands in this section.

To change table configuration(column name, metadata) - **alter table**
To change data in the database - **update table**

### Task-1
#### Alter Table

###### Add Column
- To add a new column:
```sh
alter table table_name add column_1 datatype_1;
```
###### Delete Column
- To delete a column:
```sh
alter table table_name drop column column_1;
```
###### Change datatype of a column
- To change datatype of already existing column:
> **Note:** Enter the modified datatype.
```sh
alter table table_name modify column column_1 datatype_1;
```
### Task-2
#### Update Table
The already inserted rows of data can also be modified using update table.
- General Syntax:
```sh
update table_name set column_1 = value,column_2 = value where condition;
```

<details>
  <summary>Hint</summary>
  
  ```javascript
  update student set student_id = "AC102",Course_ID=2, Course_Name = "Biology" where first_name="karan";
  ```
</details>

> **Note:** Where clause is used to identify the particular row/rows that will be updated with the column value.


## Activity - 2

Now, that you are well acquainted with table creation,update and insert commands. You can take the next step ahead. 
SQL stands for **Structured Query Language** .Query is essential to learn as you wont be working with the whole data at a time. You need to be able to extract and evaluate data on the basis of conditions. 
To understand this better, Take example of a students database in school. A teacher has marks database of around 600 students. They need to give away awards to the 90% above scorers. Now, think how difficult it would be to go through the whole table of marks and calculate the percentage indiviually and get the names of te students who scored above 90%.
This task can be done effortlessly if you know how to make queries on given conditions.

I hope you understand what exactly queries are used for. We will be learning about **clause**. Clause are basically used to add conditions to your general select command. It allows you filter the data according to your condition mentioned throught the clause.
There are 5 clause used in MySQL, namely:
- **WHERE**
-  **ORDER BY**
-  **HAVING**
-  **GROUP BY**
-  **TOP**


With this you will be completing the basics of MySQL.
### Task-1
#### WHERE
Where as the name suggests , is used to filter data according to given condition on columns. It can be where name = "albert" , marks>90 etc.
- General Syntax:

```sh
select * from table_name where course_name="accountancy";
```
> **Note-** The operators =,>=,<=,LIKE,IN, and BETWEEN can be used in where clause. The strings are compared in "". The numeric can be simply be (=10) without "".

Activity- Learn more about **LIKE** , **IN** , and **BETWEEN** .

### ORDER BY
It is used to display result in sorted order be it ascending or descending order. 
```sh
select * from student order by first_name asc|desc; 
```
### HAVING
Having clause has similar functionality that of where clause. It is used with aggregate functions because where clause cannot be used with aggregate function.
```sh
select * from student having count(Course_ID)>10;
```
It will show the details of courses having more than 10 enrollments.

### GROUP BY
Group by is generally used to group items according to a given column.
For example: You want to know the number of students from the student table. You can see there can be rows of same student with multiple courses. So group by will return the list of all unique students if you group by Student_ID as it is unique for each student.
```sh
Select * from student group by Student_ID;
```
### TOP
There can be 100s of rows of data in your table. TOP allows you to view limited number of rows as the output, say it top 50 rows, 60 rows as result.
> **Note**: In MySQL we use the keyword "limit" and mention the number of rows to show the result.
```sh
select * from student limit 5;
```

## Activity - 3

- Create a database of your name.
- Use or enter into **your_name** database.
- Create table named "**course**".
- The columns will be as follows:

| Columns  | Datatype|
| --- | ---|
|Course_ID | Varchar(20) |
|Course_Name | Varchar(40) |
|Professor | Varchar(40) |
|Duration(in months) | Int |

- Check that the table is created and it's metadata using **describe** command.
- Insert 4-5 rows of data.
- View your table. [Hint: SELECT command]

### Trivia

- Learn about BLOB, SET and ENUM datatype.
You will come across various kinds of data in real world. It is important to know about datatypes that are available to store the data of your preference. You can design you schema using these datatypes also along with the basic datatypes.
    - https://dev.mysql.com/doc/refman/8.0/en/enum.html
    - https://dev.mysql.com/doc/refman/8.0/en/blob.html
    - https://dev.mysql.com/doc/refman/8.0/en/set.html
- Explore more about date and time datatypes.
You can store date and time in many different formats.
    - https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html

## Activity - 4
- Add a new column to the course table named **"Stream"**.
- Update the table by setting the stream as "commerce" for "accountancy" course.
- Insert a new course name "History" with course ID = 101, Professor name - Mathew, and duration 6 months.
- Update the table by setting the the duration of the last added row to 3 months and stream "arts".
- Delete the stream column.

## Trivia

- Learn to use AND, OR and NOT operators. They can be combined with where clause.
- Learn about LIKE, WILDCARDS AND IN.

## Activity - 5
- Insert the dummy data:

|Course_ID|Course_Name| Professor|Duration| Stream|
| --- | --- | ---| --- | --- |
|C101|Accountancy|Matthew|4|Commerce|
|C102|Biology|Steward|7|Science|
|C105|Mathematics|Joseph|8|Science|
|C107|Physics|Harry|8|Science|
|C103|Chemistry|john|8|Science|
|C1010|History|catherine|3|Arts|
|C104|Politics|Joshua|5|Arts|
|C106|Economics|jaspreet|6|Commerce|
|C109|Sociology|Ruby|5|Arts|
|C108|Business studies|montana|3|Commerce|

- query the details of courses with duration greater than 6 months.
expected output-

|Course_ID|Course_Name| Professor|Duration| Stream|
| --- | --- | ---| --- | --- |
|C102|Biology|Steward|7|Science|
|C105|Mathematics|Joseph|8|Science|
|C107|Physics|Harry|8|Science|
|C103|Chemistry|john|8|Science|

- Query the courses in ascending order by course_id.
- Query the top 5 results order by stream in descending order.
## Trivia
What should be the order of writing the clause if you use all the clause at the same time? Find out.

## Extra Reads
- https://www.ibm.com/cloud/learn/relational-databases
- https://aws.amazon.com/relational-database/

# Congratulations!! You have successfully completed the basics of MySQL byte.






























