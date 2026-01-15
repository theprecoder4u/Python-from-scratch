# Simple Billing Counter Program

items = []
total = 0.0

print("=== Billing Counter ===")

while True:
    name = input("Enter item name (or 'done' to finish): ")

    if name.lower() == "done":
        break

    price = float(input("Enter item price: "))
    quantity = int(input("Enter quantity: "))

    cost = price * quantity
    items.append((name, price, quantity, cost))
    total += cost

    print(f"{name} added successfully!\n")

print("\n===== BILL =====")
print("Item\tPrice\tQty\tTotal")

for item in items:
    print(f"{item[0]}\t{item[1]}\t{item[2]}\t{item[3]}")

print("-------------------------")
print(f"Grand Total: ₹{total}")
print("=========================")
print("Thank you! Visit again.")
