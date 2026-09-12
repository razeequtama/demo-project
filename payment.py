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


# MODIFIED FUNCTION
# ------------------------------
# The function now accepts customer_type.
#
# This is different from Commit 2 because
# we added a new parameter.
def process_payment(
    amount,
    currency,
    customer_type="standard",
    payment_method="card"
):

    # Reject invalid payment amounts.
    if amount<= 0:
        return False

    # Check that the currency is supported.
    if not validate_currency(currency):
        return False

    # NEW CHANGE:
    # Check that the payment method
    # is supported.
    if not validate_payment_method(payment_method):
        return False

    # Calculate the transaction fee.
    if currency== "USD":
        fee= amount* 0.02

    elif currency== "EUR":
        fee= amount* 0.03

    else:
        fee= amount* 0.05

    # Calculate the customer discount.
    discount= calculate_discount(
        amount,
        customer_type
    )

    # Calculate final transaction amount.
    total= amount+ fee- discount

    # NEW CHANGE:
    # Display which payment method is being used.
    print(
        "Processing:",
        total,
        "using",
        payment_method
    )

    return True

# NEW FUNCTION
# ------------------------------
# Calculates a discount based on
# the type of customer.
def calculate_discount(amount, customer_type):

    # Premium customers receive a 10% discount.
    if customer_type== "premium":
        return amount* 0.10

    # Students receive a 5% discount.
    if customer_type== "student":
        return amount* 0.05

    # Standard customers receive no discount.
    return 0

# NEW FUNCTION
# ------------------------------
# Checks whether the payment method
# is supported by the application.
def validate_payment_method(method):

    # Payment methods supported by
    # our demo application.
    supported= [
        "card",
        "bank_transfer",
        "paypal"
    ]

    # Return True if the supplied method
    # is in our supported list.
    return method in supported