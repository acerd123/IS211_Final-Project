from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(200), nullable=False)
    page_count = db.Column(db.Integer)
    average_rating = db.Column(db.Float)

# Function to fetch book details from Google Books API
def fetch_book_by_isbn(isbn):
    url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if "items" in data and len(data["items"]) > 0:
            book = data["items"][0]["volumeInfo"]
            return {
                "title": book.get("title", "Unknown"),
                "author": ", ".join(book.get("authors", [])),
                "page_count": book.get("pageCount", "Unknown"),
                "average_rating": book.get("averageRating", "No Rating"),
            }
        else:
            return {"error": "No book found for this ISBN"}
    else:
        return {"error": "API Error"}

# Route for the homepage
@app.route("/")
def index():
    books = Book.query.all()
    return render_template("index.html", books=books)

# Route to add a book by ISBN
@app.route("/add", methods=["POST"])
def add_book():
    isbn = request.form.get("isbn")
    book_data = fetch_book_by_isbn(isbn)
    if "error" not in book_data:
        new_book = Book(
            title=book_data["title"],
            author=book_data["author"],
            page_count=book_data["page_count"],
            average_rating=book_data["average_rating"]
        )
        db.session.add(new_book)
        db.session.commit()
    return redirect(url_for("index"))

# Route to delete a book by ID
@app.route("/delete/<int:book_id>", methods=["POST"])
def delete_book(book_id):
    book = Book.query.get(book_id)
    if book:
        db.session.delete(book)
        db.session.commit()
    return redirect(url_for("index"))

# HTML template rendered dynamically
@app.route("/templates/index.html")
def templates_index_html():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Book Catalogue</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            ul { list-style: none; padding: 0; }
            li { margin: 10px 0; }
            form { display: inline; }
        </style>
    </head>
    <body>
        <h1>My Book Catalogue</h1>
        <form method="POST" action="/add">
            <input type="text" name="isbn" placeholder="Enter ISBN" required>
            <button type="submit">Add Book</button>
        </form>
        <ul>
            {% for book in books %}
                <li>
                    <strong>{{ book.title }}</strong> by {{ book.author }}
                    (Pages: {{ book.page_count }}, Rating: {{ book.average_rating }})
                    <form method="POST" action="/delete/{{ book.id }}">
                        <button type="submit">Delete</button>
                    </form>
                </li>
            {% endfor %}
        </ul>
    </body>
    </html>
    """

# Initialize the database and run the app
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
