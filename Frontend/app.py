from flask import Flask, request, jsonify, render_template, url_for
from waitress import serve

app = Flask(__name__)
BACKEND_URL = "http://localhost:8005" #To be updated using vagrant defined host/IP

#Routes to serve the main pages
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reserve')
def reserve():
    return render_template('reserve.html')

@app.route('/reservations')
def reservations():
    return render_template('reservations.html')


if __name__ == '__main__':
    serve(app,listen='*:8008')
