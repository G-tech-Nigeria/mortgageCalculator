# calculations.py - Contains functions for mortgage calculations

# TODO: Implement calculation for monthly mortgage payment
def calculate_monthly_payment(principal, interest_rate, period):
    """
    Calculate the monthly mortgage payment.

    Args:
        principal (float): The principal amount of the loan.
        interest_rate (float): The annual interest rate (in decimal form) of the loan.
        period (int): The term of the loan in months.

    Returns:
        float: The calculated monthly mortgage payment.
    """
    # Calculate monthly interest rate
    monthly_interest_rate = interest_rate / 12

    # Calculate monthly mortgage payment
    numerator = principal * monthly_interest_rate
    denominator = 1 - (1 + monthly_interest_rate) ** (-period)
    monthly_payment = numerator / denominator

    return monthly_payment

# TODO: Implement calculation for total interest paid
def calculate_total_interest(principal, interest_rate, period):
    """
    Calculates the total interest paid over the course of the mortgage
    based on the principal amount, interest rate, and loan period.

    Args:
        principal (float): The principal amount of the mortgage.
        interest_rate (float): The annual interest rate of the mortgage.
        period (int): The loan period in years.

    Returns:
        float: The calculated total interest paid.
    """
    # Convert period to months
    period = period * 12

    # Calculate monthly interest rate
    monthly_interest_rate = interest_rate / 12

    # Calculate total interest paid
    numerator = monthly_interest_rate * principal
    denominator = 1 - (1 + monthly_interest_rate) ** (-period)
    total_interest = (numerator / denominator) - principal

    return total_interest


# TODO: Implement other necessary mortgage calculations
