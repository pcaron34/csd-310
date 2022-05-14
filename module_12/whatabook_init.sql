/*
Paul Caron
5-13-2022
Module 10, 11, 12 whatabook project
*/

--CREATE A TABLE
DROP TABLE IF EXISTS books;
CREATE TABLE books (
  book_id INT AUTO_INCREMENT,
  book_name VARCHAR(200),
  details VARCHAR(500),
  author VARCHAR(200),
  PRIMARY KEY (book_id)
)

DROP TABLE IF EXISTS store;
CREATE TABLE store (
  store_id INT(50),
  locale VARCHAR(100)
)

DROP TABLE IF EXISTS users;
CREATE TABLE users (
  user_id INT NOT NULL AUTO_INCREMENT,
  first_name VARCHAR(75),
  last_name VARCHAR(75),
  PRIMARY KEY (user_id)

DROP TABLE IF EXISTS wishlist;
CREATE TABLE wishlist (
  user_id INT,
  book_id VARCHAR(75),
  wishlist_id INT
)

-- Insert books into books table
INSERT INTO books(author, book_id, book_name, details)
  VALUES('James McPherson', '100', 'Battle Cry of Freedom: The Civil War Era', 'very long list');

INSERT INTO books(author, book_id, book_name, details)
  VALUES('Michael Shaara', '101', 'The Killer Angels', 'still to long to list');

INSERT INTO books(author, book_id, book_name, details)
  VALUES('Tony Horwitz', '102', 'Confederates in the Attic', 'thought you knew');

INSERT INTO books(author, book_id, book_name, details)
  VALUES('Eric Foner', '103', 'The Fiery Trial', 'fine it has a picture of Abe Lincoln on the cover');

INSERT INTO books(author, book_id, book_name, details)
  VALUES('David Blight', '104', 'Race and Reunion', 'nope');

INSERT INTO books(author, book_id, book_name, details)
  VALUES('Ron Chernow', '105', 'Grant', 'Along time ago in the Milky Way');

INSERT INTO books(author, book_id, book_name, details)
  VALUES('S.C. Gwynne', '106', 'Rebel Yell', 'a little of this, a little of that');

INSERT INTO books(author, book_id, book_name, details)
  VALUES('Shelby Foote', '107', 'The Civil War', 'a book on the civil war');

INSERT INTO books(author, book_id, book_name, details)
  VALUES('Stephen Crane', '108', 'The Red Badge of Courage', 'not the cowardly lion');

-- Insert stores into store table
INSERT INTO store(store_id, locale)
  VALUES('1', '1234 Foxconn Rd SuperSmallTown, NE 68999');

-- Insert users into user table
INSERT INTO users(user_id, first_name, last_name)
  VALUES('11', 'George', 'Rockwell');

INSERT INTO users(user_id, first_name, last_name)
  VALUES('12', 'Matt', 'Koehl');

INSERT INTO users(user_id, first_name, last_name)
  VALUES('13', 'Rocky', 'Suhayda');

-- Insert items into wishlist table
INSERT INTO wishlist(user_id, book_id, wishlist_id)
  VALUES('11', '101', '1');

INSERT INTO wishlist(user_id, book_id, wishlist_id)
  VALUES('13', '104', '2');

INSERT INTO wishlist(user_id, book_id, wishlist_id)
  VALUES('12', '108', '3');

-- Delete store from store table
--DELETE FROM store(store_id)
--  VALUES('1');

   