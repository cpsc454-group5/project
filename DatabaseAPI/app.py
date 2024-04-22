from flask import Flask, request, jsonify
from waitress import serve
import secrets
import datetime
import sqlite3

app = Flask(__name__)

# Function to generate an expiring token
def generate_token():
    token = secrets.token_hex(16)
    expiration = datetime.datetime.now() + datetime.timedelta(minutes=30)  # Token expires in 30 minutes
    return token, expiration

# Function to store token in database
def store_token_in_database(token, expiration, book_id):
    # Connect to the database
    conn = sqlite3.connect('books.db')
    c = conn.cursor()
    # Insert token and expiration into database
    c.execute("INSERT INTO Tokens (token, expiration, book_id) VALUES (?, ?, ?)", (token, expiration, book_id))
    # Commit changes and close connection
    conn.commit()
    conn.close()

# Function to clean up expired tokens from database
def clean_up_expired_tokens():
    # Connect to the database
    conn = sqlite3.connect('books.db')
    c = conn.cursor()
    # Delete expired tokens from database
    c.execute("DELETE FROM Tokens WHERE expiration < ?", (datetime.datetime.now(),))
    # Commit changes and close connection
    conn.commit()
    conn.close()

# API endpoint to request a book link with expiring token
@app.route('/request', methods=['GET'])
def request_book_link():
    book_id = request.args.get('bookid')
    token, expiration = generate_token()
    store_token_in_database(token, expiration, book_id)
    link = f"/books/{book_id}?token={token}"
    return jsonify({'link': link})

# API endpoint to verify token and bookid
@app.route('/verify', methods=['GET'])
def verify_token():
    token = request.args.get('token')
    book_id = request.args.get('bookid')
    # Clean up expired tokens before verification
    clean_up_expired_tokens()
    # Fetch token and expiration from database based on book_id
    conn = sqlite3.connect('books.db')
    c = conn.cursor()
    c.execute("SELECT expiration FROM Tokens WHERE token = ? AND book_id = ?", (token, book_id))
    result = c.fetchone()
    conn.close()
    if result:
        time=datetime.datetime.strptime(result[0], "%Y-%m-%d %H:%M:%S.%f")
        if time > datetime.datetime.now():
            return jsonify({'verified': True})
    return jsonify({'verified': False})

# API endpoint to search for books by name or author
@app.route('/search', methods=['GET'])
def search_books():
    keyword = request.args.get('keyword')
    # Query database for books matching keyword in book_name or book_author
    conn = sqlite3.connect('books.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Books WHERE book_name LIKE ? OR book_author LIKE ?", ('%' + keyword + '%', '%' + keyword + '%'))
    books = [{'book_name': row[1], 'book_author': row[2], 'book_id': row[0]} for row in c.fetchall()]
    conn.close()
    return jsonify({'books': books})

# API endpoint to list count number of books
@app.route('/list', methods=['GET'])
def list_books():
    count = int(request.args.get('count'))
    # Query database for count number of books
    conn = sqlite3.connect('books.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Books LIMIT ?", (count,))
    books = [{'book_name': row[1], 'book_author': row[2], 'book_id': row[0]} for row in c.fetchall()]
    conn.close()
    return jsonify({'books': books})


if __name__ == '__main__':
    serve(app,listen='*:8005')
