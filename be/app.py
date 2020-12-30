from flask import Flask, jsonify, request
from paymentIntent import getPaymentIntent
from flask_cors import CORS, cross_origin


app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"/": {"origins": "http://localhost:3000"}})


@app.route('/secret')
@cross_origin(origin='localhost',headers=['Content-Type'])
def secret():
  intent = getPaymentIntent(1099)
  return jsonify(client_secret=intent.client_secret)


@app.route('/confirm')
@cross_origin(origin='localhost',headers=['Content-Type'])
def confirm():
  return 'Status: ' + request.args.get('redirect_status')