from flask import Flask, request, jsonify, render_template, url_for, redirect
import requests
from waitress import serve

app = Flask(__name__)
BACKEND_URL = "http://localhost:8005" #To be updated using vagrant defined host/IP

#Routes to serve the main pages
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reserve')
def reserve():
    resp = requests.request('GET', BACKEND_URL + '/list?count=' + f'10')
    bookList = ''
    availList = ''
    for book in resp.json()['books']:
        bookList += ('<li><div class="liTitle">Title: </div>')
        bookList += (f'<div>{book["book_name"]}</div>')
        bookList += (f'<div class="vl push"></div>')
        bookList += (f'<div>Reservable copies: </div>')
        if book['reserved_by'] == None:
            bookList += (f'<div class="digSize">1</div></li>')
            availList += (f'<option value=\"' + f'{book["book_id"]},{book["book_name"]}' + f'\">{book["book_name"]}</option>')
        else:
            bookList += (f'<div class="digSize">0</div></li>')
    return render_template('reserve.html', books=bookList, available=availList)

@app.route('/reservations')
def reservations():
    resp = requests.request('GET', BACKEND_URL + '/list?count=' + f'10')
    bookList = ''
    for book in resp.json()['books']:
        if book['reserved_by'] != None:
            bookList += ('<li><div class="liTitle">Title: </div>')
            bookList += (f'<div>{book["book_name"]}</div>')
            bookList += (f'<div class="vl push"></div>')
            bookList += (f'<div>Reserved By: </div>')
            bookList += (f'<div class="nSize">{book["reserved_by"]}</div></li>')
    if not bookList:
        bookList = '<li><div class="liTitle">No Active Reservations</div></li>'
    return render_template('reservations.html', books=bookList)

@app.route('/makeReserve', methods=['GET'])
def reserveBook():
    fName = request.args.get('fName')
    lName = request.args.get('lName')
    fullName = fName + '%20' + lName
    bookInfo = request.args.get('bookTitle').split(',')
    resp = requests.request('GET', BACKEND_URL + f'/request?bookid={bookInfo[0]}&username={fullName}')
    print(resp)
    return redirect('/reservations')

if __name__ == '__main__':
    serve(app,listen='*:8008')
