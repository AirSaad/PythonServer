from flask import Flask, jsonify, request
import stripe

# Initialize Flask app
app = Flask(__name__)

# Set up your Stripe secret key (replace with your own secret key)
stripe.api_key = 'sk_test_51QURhPAx2perfVvzUYkzy2ciZBrW9JpLnY7S7WJlzfrGK2DPZuOCX9aiRkQvJvtUMr9PzQCAXdyCCSGxlMtdo2mO00fdoFx0Ge'  # Replace with your actual Stripe Secret Key


# Create a simple route to check if the server is running
@app.route('/')
def index():
    return "Stripe API server is running!"


# Endpoint to create a PaymentIntent
@app.route('/create-payment-intent', methods=['POST'])
def create_payment_intent():
    try:
        # Get data from the request body (amount and currency)
        data = request.get_json()
        amount = data['amount']
        currency = data['currency']

        # Create the payment intent using Stripe API
        payment_intent = stripe.PaymentIntent.create(
            amount=amount,
            currency=currency,
            payment_method_types=["card"]
        )

        # Return the client secret to the frontend
        return jsonify({
            'clientSecret': payment_intent.client_secret
        })

    except Exception as e:
        # Return error message if something goes wrong
        return jsonify({'error': str(e)}), 400


# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
