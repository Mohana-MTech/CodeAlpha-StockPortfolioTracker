import csv

portfolio = []  # list to store stock details

def add_stock():
    print("\n=== Add Stock ===")
    name = input("Stock Name: ").upper()
    qty = int(input("Quantity: "))
    price = float(input("Price per Share: "))
    total = qty * price

    portfolio.append({
        "Stock": name,
        "Quantity": qty,
        "Price": price,
        "Total": total
    })

    print(f" {name} added successfully!")

def view_portfolio():
    print("\n=== Portfolio Details ===")
    if not portfolio:
        print("No stocks added yet.")
    else:
        grand_total = 0
        for stock in portfolio:
            print(f"Stock: {stock['Stock']} | Quantity: {stock['Quantity']} | "
                  f"Price: {stock['Price']:.2f} | Total: {stock['Total']:.2f}")
            grand_total += stock['Total']
        print(f"\n Portfolio Value: {grand_total:.2f}")

def save_report():
    with open("portfolio.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["Stock", "Quantity", "Price", "Total"])
        writer.writeheader()
        writer.writerows(portfolio)
    print(" Portfolio report saved successfully as 'portfolio.csv'!")

def main():
    while True:
        print("\n===== Stock Portfolio Tracker =====")
        print("1. Add Stock")
        print("2. View Portfolio")
        print("3. Save Report")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_stock()
        elif choice == "2":
            view_portfolio()
        elif choice == "3":
            save_report()
        elif choice == "4":
            print("Exiting Stock Portfolio Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
