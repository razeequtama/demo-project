# NEW FUNCTION
# ------------------------------
# This function checks whether the
# supplied currency is supported.
def validate_currency(currency):

    # List of currencies currently supported
    # by our demo payment system.
    supported= [
        "USD",
        "EUR",
        "GBP",
        "JPY"
    ]

    # Return True if the currency exists
    # in our supported-currency list.
    return currency in supported


# EXISTING FUNCTION
# ------------------------------
# This function already existed in
# Commit 1, but we are modifying it.
def process_payment(amount, currency):

    # Reject invalid payment amounts.
    if amount<= 0:
        return False

    # NEW CHANGE:
    # Before processing the payment,
    # make sure the currency is supported.
    if not validate_currency(currency):
        return False

    # Calculate the transaction fee.
    if currency== "USD":
        fee= amount* 0.02

    elif currency== "EUR":
        fee= amount* 0.03

    else:
        # GBP, JPY, and other supported currencies
        # currently use a 5% fee.
        fee= amount* 0.05

    # Calculate the final payment amount.
    total= amount+ fee

    # Display the transaction.
    print("Processing:", total)

    # Payment was processed successfully.
    return True