CREATE TABLE IF NOT EXISTS book (
    book_id SERIAL,
    title   VARCHAR(255) NOT NULL,
    author  VARCHAR(255) NOT NULL,
    rating  INT          NOT NULL,
    PRIMARY KEY (book_id)
);

INSERT INTO book (title, author, rating)
VALUES
	('The Hobbit', 'J.R.R. Tolkien', 5),
	('Imbibe', 'David Wondrich', 4),
	('The Picture of Dorian Gray', 'Oscar Wilde', 2)
;
