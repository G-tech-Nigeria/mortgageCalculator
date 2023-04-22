# validation.py - Contains functions for input validation

def validate_mortgage_input(principal, interest_rate, period):
    """
    Validate the input data for the mortgage calculator.

    Args:
        principal (float): The principal amount of the loan.
        interest_rate (float): The annual interest rate (in decimal form) of the loan.
        period (int): The period of the loan in months.

    Returns:
        bool: True if input data is valid, False otherwise.
    """
    # Check if principal is a positive number
    if principal <= 0:
        return False

    # Check if interest rate is within a valid range (0 to 1)
    if interest_rate < 0 or interest_rate > 1:
        return False

    # Check if period is a positive integer
    if not isinstance(period, int) or period <= 0:
        return False

    # Input data is valid
    return True

# TODO: Implement other necessary input validation functions
# ...
