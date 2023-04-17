create table items(
id serial primary key,
item varchar(100),
price varchar(10)
);	
insert into items (item, price) values
( 'Small Desk', '100'), 
( 'Large desk', '300'),
( 'Fan', '80'); 


create table customers (
id serial primary key,
name1 varchar(50),
name2 varchar(50)
);		
insert into customers (name1, name2) values
( 'Greg', 'Jones'), 
( 'Sandra ', 'Jones'), 
( 'Scott ', 'Scott '), 
( 'Trevor ', 'Green'), 
( 'Melanie ', 'Johnson');


create table items (
  id serial primary key,
  item varchar(100),
  price varchar(10)
);	
insert into items (item, price) values
( 'Small Desk', '100'), 
( 'Large desk', '300'), 
( 'Fan', '80'); 

create table customers (
  id serial primary key,
  name1 varchar(50),
  name2 varchar(50)
);		
insert into customers (name1, name2) values
( 'Greg', 'Jones'), 
( 'Sandra', 'Jones'), 
( 'Scott', 'Scott'), 
( 'Trevor', 'Green'), 
( 'Melanie', 'Johnson');



ALTER TABLE items ALTER COLUMN price TYPE integer USING price::integer;
SELECT * FROM public.items where price>80;
SELECT * FROM public.items where price<300;
SELECT * FROM public.customers where name2='Smith';
SELECT * FROM public.customers where name1 NOT LIKE 'Scott%';

















