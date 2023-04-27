# TODO: 1.The calculator should allow users to enter the amount of the loan they are considering.
# TODO: 2.The calculator should allow users to enter the interest rate they are being offered.
# TODO: 3. The calculator should allow users to select the term of the loan, such as 15 years, 20 years, etc.
# TODO: 4.The calculator should display the estimated monthly mortgage payments based on the inputs provided

# app.py - Main application file for the mortgage calculator API

from flask import Flask, request, jsonify, render_template
from calculations import calculate_monthly_payment
from validation import validate_mortgage_input


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate-mortgage-payment', methods=['POST'])
def calculate_mortgage_payment():
    # Parse request data
    principal = float(request.form['principal'])
    interest_rate = float(request.form['interest_rate'])
    period = int(request.form['loan_term']) * 12  # Convert loan term from years to months

    # Validate input data
    if not validate_mortgage_input(principal, interest_rate, period):
        # Return error response for invalid input data
        response = {
            'error': 'Invalid input data'
        }
        return jsonify(response), 400

    # Calculate monthly mortgage payment
    monthly_payment = calculate_monthly_payment(principal, interest_rate, period)

    # Return response
    response = {
        'principal': principal,
        'interest_rate': interest_rate,
        'loan_term': int(period / 12),  # Convert loan period from months to years
        'monthly_payment': monthly_payment
    }
    return jsonify(response), 200


if __name__ == '__main__':
    app.run(debug=True)
