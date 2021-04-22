select * from items

select * from Users

drop table items

create table items(
ID int identity(1,1) primary key,
userId int not null,
item varchar(200) not null)

create table Users(
Id int identity(1,1) primary key,
FName varchar(20) not null,
LName varchar(20) not null,
UName varchar(20) not null,
Email varchar(40) not null,
Password varchar(max) null)

declare @id int;

set @id = (select Id from Users where Email = 'rohitvemula@gmail.com')

insert into items (userId, item)
values (@id, 'task101');


--
id = Select



--

select Id from Users where Email = 'rohitvemula@gmail.com'


ALTER TABLE items
ALTER COLUMN ID varchar(10);