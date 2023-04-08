use todo;  -- Name of the database 

show tables;  -- to list down all tables

-- to create a table named: todos
create table todos(sno int primary key AUTO_INCREMENT, title varchar(100), descb varchar(200), date_created varchar(20));

desc todos;   -- to describe the table named todos

-- inserting rows/data into todos table
insert into todos values(1, "Buy Groceries", "Mango, Brinjal, Tomato Buy karna hai", "28th March");

insert into todos values(2, "Study JavaScript", "Callback functions, Arrow functions", "29th March");

select * from todos;  -- to display all data from the todos table

drop table todos;     -- to delete/remove todos table from database
