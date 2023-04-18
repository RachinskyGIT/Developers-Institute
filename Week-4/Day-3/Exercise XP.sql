-- Exercise 1: DVD Rental


-- select title, description, language_id from film

-- SELECT DISTINCT language_id FROM film;

-- create table new_film (
-- 	id INT PRIMARY KEY,
-- 	name varchar(100) not null
-- );

-- create table customer_review (
-- 	review_id  INT PRIMARY KEY not null,
-- 	film_id INT REFERENCES new_film(id) ON DELETE CASCADE,
-- 	language_id INT REFERENCES language(language_id),
-- 	title varchar(100) not null,
-- 	score INT CHECK (score  BETWEEN 1 AND 10),
-- 	review_text varchar not null,
-- 	last_update TIMESTAMP DEFAULT NOW()
-- );

-- INSERT INTO new_film (id, name) VALUES (1, 'The Shawshank Redemption');
-- INSERT INTO new_film (id, name) VALUES (2, 'The Godfather'), (3, 'The Dark Knight');
-- INSERT INTO new_film (id, name) VALUES (4, 'Stupid Film');

-- INSERT INTO customer_review (review_id, film_id, language_id, title, score, review_text)
-- VALUES (1, 1, 1, 'Great movie!', 9, 'I really enjoyed this movie. The acting was fantastic and the plot was well-developed.');

-- INSERT INTO customer_review (review_id, film_id, language_id, title, score, review_text)
-- VALUES (2, 2, 1, 'Classic film', 10, 'The Godfather is a true classic. The acting, directing, and storytelling are all top-notch.');

-- delete from new_film where id = 1;


-- select * from new_film;
-- select * from customer_review



-- Exercise 2 : DVD Rental


-- UPDATE film
-- SET language_id = 2
-- WHERE film_id=133;

-- select * from film


-- SELECT COUNT(*) AS num_outstanding_rentals
-- FROM rental
-- WHERE return_date IS NULL;

-- SELECT f.title, f.replacement_cost
-- FROM film f
-- INNER JOIN inventory i ON f.film_id = i.film_id
-- INNER JOIN rental r ON i.inventory_id = r.inventory_id
-- WHERE r.return_date IS NULL
-- ORDER BY f.replacement_cost DESC
-- LIMIT 30;


-- SELECT title
-- FROM film
-- WHERE to_tsvector('english', fulltext::text) @@ to_tsquery('english', 'sumo&wrestler')
-- AND film_id IN (
--   SELECT film_id 
--   FROM film_actor 
--   WHERE actor_id IN (
-- 	  SELECT actor_id 
-- 	  FROM actor 
-- 	  WHERE first_name='Penelope' and last_name = 'Monroe'
-- 	)
-- );


SELECT title
FROM film
WHERE to_tsvector('english', fulltext::text) @@ to_tsquery('english', 'documentary') 
AND length<60 
AND rating='R'
