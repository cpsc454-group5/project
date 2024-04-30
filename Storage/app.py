from flask import Flask, request, jsonify, send_file
from waitress import serve
import requests

app = Flask(__name__)
DATABASE_SERVER_URL = "http://localhost:8005" #To be updated using vagrant defined host/IP

@app.route('/books/<int:book_id>', methods=['GET'])
def retrieve_book(book_id):
    token = request.args.get('token')

    # Verify token and book_id by making a request to the database server
    verify_url = f"{BOOK_SERVER_URL}/verify?token={token}&book_id={book_id}"
    response = requests.get(verify_url)

    if response.text != "Failed":
        filename = response.text
        # Assuming book files are stored in a directory named "books"
        return send_file(f"books/{filename}")
    else:
        return jsonify({"error": "Invalid token or book ID"})

if __name__ == '__main__':
    app.run(host='localhost', port=8007)
