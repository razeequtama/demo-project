def process_payment(amount, currency):

    if amount <= 0:
        return False

    if currency == "USD":
        fee = amount * 0.02

    elif currency == "EUR":
        fee = amount * 0.03

    else:
        fee = amount * 0.05

    total = amount + fee

    print("Processing:", total)

    return True