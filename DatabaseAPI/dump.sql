-- Schema
CREATE TABLE Books (
    book_id SERIAL PRIMARY KEY,
    book_name VARCHAR(255),
    book_author VARCHAR(255),
    book_filename VARCHAR(255)
);

-- Sample data
INSERT INTO Books (book_id,book_name, book_author, book_filename) VALUES
(1,'Pride and Prejudice', 'Jane Austen', 'pride_and_prejudice.txt'),
(2,'To Kill a Mockingbird', 'Harper Lee', 'to_kill_a_mockingbird.pdf'),
(3,'1984', 'George Orwell', '1984.txt'),
(4,'The Great Gatsby', 'F. Scott Fitzgerald', 'the_great_gatsby.txt');

CREATE TABLE Tokens (
    token_id INTEGER PRIMARY KEY,
    token VARCHAR(255),
    expiration DATETIME,
    user_name VARCHAR(255),
    book_id INTEGER,
    FOREIGN KEY (book_id) REFERENCES Books(book_id)
);

