from flask import Flask, jsonify
from .paymentIntent import getPaymentIntent
app = Flask(__name__)

@app.route('/secret')
def secret():
  intent = getPaymentIntent(1099)
  return jsonify(client_secret=intent.client_secret)