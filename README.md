This web application is built using Flask and SQLAlchemy, allowing users to maintain a catalogue of books. It provides the ability to add books by ISBN, view their details, and delete them from the catalogue. The application fetches book information from the Google Books API, which provides metadata such as the title, author(s), page count, and average rating for each book. This ensures that users don’t have to manually enter all the details for each book, simplifying the process of cataloging books.

The core of the application is the Book model, which is defined using SQLAlchemy. This model has five fields: id (the primary key, which is auto-incremented), title (the book's title), author (the author(s) of the book), page_count (the total number of pages), and average_rating (the book’s average rating if available). The app uses a SQLite database (books.db), where all books are stored. The database is initialized when the application runs, and the necessary tables are created automatically using SQLAlchemy’s create_all() method.

The main functionality is driven by three routes: the home page (/), which displays the books currently in the catalogue and allows users to add a new book via ISBN; the /add route, which handles the submission of an ISBN, fetches book data from the Google Books API, and stores the book details in the database; and the /delete/<int:book_id> route, which allows users to delete books from the catalogue by their unique id. The app also includes a simple /test route for verifying that Flask is working properly.

The Google Books API is used to fetch book data when a user enters an ISBN. The API response includes the book’s title, author(s), page count, and average rating, which are then displayed in the catalogue. If the book is not found or there is an error with the API, an appropriate message is displayed to the user.

The application requires Python 3.x, along with the Flask, Flask-SQLAlchemy, and Requests libraries. Users can easily install the required dependencies using a requirements.txt file. Once the dependencies are installed, the application can be run locally using Flask’s built-in server, and users can interact with the book catalogue through their web browser.

In conclusion, this Flask-based book catalogue application offers a simple yet powerful way to track a personal book collection. By integrating with the Google Books API, it simplifies the process of adding books to the catalogue, making it more efficient and user-friendly. Whether you are a casual reader or a more serious collector, this tool helps manage your books in an organized manner, ensuring easy access to essential details about each book.







