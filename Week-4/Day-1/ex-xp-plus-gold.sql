CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  first_name VARCHAR(50),
  last_name VARCHAR(50),
  birth_date DATE
);

INSERT INTO students (first_name, last_name, birth_date)
VALUES
  ('Marc', 'Benichou', '1998-11-02'),
  ('Yoan', 'Cohen', '2010-12-03'),
  ('Lea', 'Benichou', '1987-07-27'),
  ('Amelia', 'Dux', '1996-04-07'),
  ('David', 'Grez', '2003-06-14'),
  ('Omer', 'Simpson', '1980-10-03');
  

SELECT first_name, last_name FROM public.students ;
SELECT first_name, last_name FROM public.students where id=2 ;
SELECT first_name, last_name FROM public.students where  first_name LIKE 'A%' ;

SELECT * FROM students
WHERE first_name LIKE '%a%' AND
      first_name NOT LIKE 'a%' AND
      first_name NOT LIKE '%a' AND
      SUBSTRING(first_name, 2, LENGTH(first_name)-2) LIKE '%a%';


SELECT * FROM students
WHERE birth_date >= '2000-01-01'


SELECT * 
FROM students 
ORDER BY last_name 
LIMIT 4;

SELECT * 
FROM students 
ORDER BY birth_date DESC 
LIMIT 1;


SELECT *
FROM students
LIMIT 3 OFFSET 2;







