	CREATE DATABASE CRIO;
    USE CRIO;
    create table customer(id int primary key , full_name varchar(10) not null, Age int,
                       contact int not null Unique, address varchar(10) default"NA");
DESC customer;
insert into customer(id , full_name , Age, contact, address)
values(1,"Nitesh",22,34434,"India");
insert into customer(id , full_name , Age, contact)
values(2,"RAM",11,334);
select * from customer;