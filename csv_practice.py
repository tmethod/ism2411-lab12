# 1 -- Python makes it easier to automate and do the same process over and over again, in excel i can use the tools they have but it takes longer - what is easier in excel is doing simple things and viewing things quicker instead of writing code

# 2 -- total sales at the end of each day - since you can add new entries without deleting older ones. 



import csv
from datetime import datetime
from pathlib import Path

# Exercise 2: Read and print the CSV file.
csv_path = Path(__file__).resolve().parent / "data" / "sales.csv"

with open(csv_path, newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Exercise 3: Read and print the CSV using next reader.
with open(csv_path, newline="") as file:
    reader = csv.reader(file)
    header = next(reader)
    print(header)
    for row in reader:
        print(row)

# Exercise 4: Compute totals
with open(csv_path, newline="") as file:
    reader = csv.reader(file)
    header = next(reader)
    total = 0
    for row in reader:
        price = float(row[1])
        quantity = int(row[2])
        revenue = price * quantity
        print(f"{row[0]}: {quantity} units × ${price:.2f} = ${revenue:.2f}")
        total += revenue
    print(f"Total revenue: ${total:.2f}")


# Exercise 5: Filter and write
output_path = Path(__file__).resolve().parent / "data" / "cleaned.csv"

with open(csv_path, newline="") as file:
    reader = csv.reader(file)
    header = next(reader)
    original_rows = list(reader)
    filtered_rows = [
        row + [f"{float(row[1]) * int(row[2]):.2f}"]
        for row in original_rows if float(row[1]) * int(row[2]) > 100
    ]

with open(output_path, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Product", "Price", "Qty", "Total"])
    writer.writerows(filtered_rows)

print(f"{len(filtered_rows)} rows written out of {len(original_rows)} original rows to {output_path}")

# Exercise 6: use DictReader

# - reader is better for simple files while dictreader is better for files with headers.


with open(csv_path, newline="") as file:
    reader = csv.DictReader(file)
    total = 0
    for row in reader:
        revenue = float(row['price']) * int(row['quantity'])
        total += revenue
        print(f"{row['product']}: {row['quantity']} units × ${float(row['price']):.2f} = ${revenue:.2f}")
    print(f"Total revenue: ${total:.2f}")

# Exercise 7: Sales summary by product
with open(csv_path, newline="") as file:
    reader = csv.DictReader(file)
    sales_by_product = {}
    for row in reader:
        product = row['product']
        quantity = int(row['quantity'])
        revenue = float(row['price']) * quantity
        if product not in sales_by_product:
            sales_by_product[product] = 0
        sales_by_product[product] += revenue

    for product in sorted(sales_by_product):
        print(f"{product}: Total revenue: ${sales_by_product[product]:.2f}")
    print(f"Overall total revenue: ${sum(sales_by_product.values()):.2f}")

# Exercise 8: Append mode log
log_path = Path(__file__).resolve().parent / "data" / "run_log.txt"

with open(log_path, "a", newline="") as file:
    file.write(f"{datetime.now()}: Total revenue: ${total:.2f}\n")

print(f"Sales log written to {log_path}")
