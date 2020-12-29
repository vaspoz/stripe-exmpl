import stripe

# Set your secret key. Remember to switch to your live secret key in production!
# See your keys here: https://dashboard.stripe.com/account/apikeys
stripe.api_key = 'sk_test_51I3POiJJCaz63LZXi9ZsEWsfT16M1gvn17uIVVYCv1KvBJzBx7KP9WN02rcIBvt6IE1qxz2MXBmxYrfVgQNCIhd900Bl6Ophv9'


def getPaymentIntent(amount):
  return stripe.PaymentIntent.create(
    amount=amount,
    currency='eur',
    payment_method_types=['ideal']
  )