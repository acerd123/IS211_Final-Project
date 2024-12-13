Overview

This is a simple web application built using Flask and SQLAlchemy that allows users to maintain a catalogue of books. Users can add books by ISBN, view their details (such as title, author, page count, and rating), and delete books from their catalogue. The book information is fetched from the Google Books API, which provides metadata such as the title, author(s), page count, and average rating for each book.

How It Works

Book Model: The application uses SQLAlchemy to define a Book model, which is used to store information about books in a SQLite database (books.db). Each book entry includes:

id: A unique identifier for each book (auto-incremented).
title: The title of the book.
author: The author(s) of the book.
page_count: The total number of pages in the book.
average_rating: The average rating of the book, if available.

Routes: /: This is the home page, which displays all books currently in the catalogue. Users can also add a new book by entering an ISBN.
/add: This route handles the submission of an ISBN, fetches the book details from the Google Books API, and stores the book in the database.
/delete/<int:book_id>: This route allows users to delete a book from the database using its unique id.
/test: A simple route to verify that Flask is running properly.

Google Books API: When a user enters an ISBN, the fetch_book_by_isbn function makes a request to the Google Books API (https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}). If the book is found, its title, author(s), page count, and average rating are returned and added to the database. If no book is found or an error occurs, an appropriate message is displayed.

Model Details

The Book model is defined using SQLAlchemy, and it includes the following fields:

id: This field is the primary key and is auto-incremented by the database.
title: This is a string that stores the title of the book (max length 200).
author: A string that stores the author(s) of the book (max length 200).
page_count: This is an integer that stores the number of pages in the book.
average_rating: This is a float that stores the average rating of the book (if available).
The database is a SQLite database (books.db), and it is initialized automatically when the application starts. The db.create_all() command is called to create the necessary tables.

