import csv
import random

# Given data
wine_types = "Syrah, Merlot, Cabernet Sauvignon, Malbec, Pinot Noir, Chardonnay, Riesling, Sauvignon Blanc, Semillon, Moscato, Pinot Grigio, Gewurztraminer, Chenin Blanc, Viognier, Verdelho, Other"
wine_types = [t.strip() for t in wine_types.split(',')]

wine_years = range(1990, 2024)
wine_manufacturers = ["Winery A", "Winery B", "Winery C", "Winery D", "Winery E"]

# Generate random data
wine_data = []
for _ in range(25):  # Adjust the number of entries as needed
    wine_entry = {
        "Year": random.choice(wine_years),
        "Manufacturer": random.choice(wine_manufacturers),
        "Type": random.choice(wine_types)
    }
    wine_data.append(wine_entry)

# Write data to CSV
csv_file = "wine_collection.csv"
with open(csv_file, "w", newline="") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["Year", "Manufacturer", "Type"])  # Write header row
    for entry in wine_data:
        csv_writer.writerow([entry["Year"], entry["Manufacturer"], entry["Type"]])

print(f"Data written to {csv_file}")
