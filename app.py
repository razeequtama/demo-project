from payment import process_payment


def main():
    print("Application started")

    process_payment(
        100,
        "USD"
    )


if __name__ == "__main__":
    main()