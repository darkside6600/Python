import csv
import time

def getLandList():
    land_file = "LandOwned.csv"
    land_list = []  
    with open(land_file, mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            land_list.append(row)
    return land_list

def calculate_earnings_per_second(item):
    rate = float(item[1])
    earnings_per_second = float(item[2])
    return rate * earnings_per_second * 1.5

total_earnings_per_second = 2.2582

# Run the simulation for 60 seconds
for _ in range(3000):
    # Refresh land data every 5 seconds
    if _ % 5 == 0:
        land = getLandList()
        common = land[0]
        rare = land[1]
        epic = land[2]
        legendary = land[3]

    total_earnings_per_second += sum([
        calculate_earnings_per_second(common),
        calculate_earnings_per_second(rare),
        calculate_earnings_per_second(epic),
        calculate_earnings_per_second(legendary)
    ])

    # Display the result for each second
    print(f"Total Earnings per Second: {total_earnings_per_second:.18f}")

    # Pause for 1 second
    time.sleep(1)
