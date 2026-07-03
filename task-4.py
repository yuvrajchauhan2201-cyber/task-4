import csv

# File names
csv_file = "salesdata.csv"
report_file = "sales_report.txt"

products = []

with open(csv_file, mode="r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["Product"]
        quantity = int(row["Quantity"])
        price = float(row["Price"])

        revenue = quantity * price

        products.append({
            "Product": product,
            "Quantity": quantity,
            "Price": price,
            "Revenue": revenue
        })

top_products = sorted(products, key=lambda x: x["Quantity"], reverse=True)[:5]

total_revenue = sum(item["Revenue"] for item in products)

min_quantity = min(item["Quantity"] for item in products)
least_products = [item for item in products if item["Quantity"] == min_quantity]

print("===== PRODUCT SALES REPORT =====\n")

print("Top 5 Selling Products:")
for i, item in enumerate(top_products, start=1):
    print(f"{i}. {item['Product']} - {item['Quantity']} units")

print(f"\nTotal Revenue: ₹{total_revenue:.2f}")

print("\nLeast Selling Product(s):")
for item in least_products:
    print(f"- {item['Product']} ({item['Quantity']} units)")

with open(report_file, "w", encoding="utf-8") as report:
    report.write("===== PRODUCT SALES REPORT =====\n\n")

    report.write("Top 5 Selling Products:\n")
    for i, item in enumerate(top_products, start=1):
        report.write(f"{i}. {item['Product']} - {item['Quantity']} units\n")

    report.write(f"\nTotal Revenue: ₹{total_revenue:.2f}\n")

    report.write("\nLeast Selling Product(s):\n")
    for item in least_products:
        report.write(f"- {item['Product']} ({item['Quantity']} units)\n")

print(f"\nReport successfully exported to '{report_file}'")