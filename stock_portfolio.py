portfolio = {}

while True:
    print("\n===== STOCK PORTFOLIO TRACKER =====")
    print("1. Add Stock")
    print("2. View Portfolio")
    print("3. Calculate Total Investment")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        stock = input("Enter stock name: ").upper()
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price per share: "))

        portfolio[stock] = {
            "quantity": quantity,
            "price": price
        }

        print("Stock added successfully!")

    elif choice == "2":
        if not portfolio:
            print("Portfolio is empty.")
        else:
            print("\n--- Your Portfolio ---")

            for stock, details in portfolio.items():
                quantity = details["quantity"]
                price = details["price"]
                value = quantity * price

                print(
                    f"{stock} | Quantity: {quantity} | "
                    f"Price: ₹{price:.2f} | Value: ₹{value:.2f}"
                )

    elif choice == "3":
        total = 0

        for details in portfolio.values():
            total += details["quantity"] * details["price"]

        print(f"Total Investment: ₹{total:.2f}")

    elif choice == "4":
        print("Thank you for using Stock Portfolio Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")