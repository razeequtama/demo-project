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
    customer_type="standard"
):

    # Reject invalid amounts.
    if amount<= 0:
        return False

    # Reject unsupported currencies.
    if not validate_currency(currency):
        return False

    # Calculate currency-specific fees.
    if currency== "USD":
        fee= amount* 0.02

    elif currency== "EUR":
        fee= amount* 0.03

    else:
        fee= amount* 0.05

    # NEW CHANGE:
    # Calculate any customer discount.
    discount= calculate_discount(
        amount,
        customer_type
    )

    # NEW CHANGE:
    # Subtract the discount from the
    # amount plus the transaction fee.
    total= amount+ fee- discount

    # Display the final amount.
    print("Processing:", total)

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