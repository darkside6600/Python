import time

# Given lists
common = ['39', '.0000000011']
rare = ['23', '.0000000016']
epic = ['12', '.0000000022']
legendary = ['7', '.0000000044']

# Function to calculate earnings per second for each category
def calculate_earnings_per_second(item):
    rate = float(item[0])  # Convert the rate to a float
    earnings_per_second = float(item[1])  # Convert earnings per second to a float
    return rate * earnings_per_second * 1.3

# Initialize total earnings per second
total_earnings_per_second = 6.8583

# Run the simulation for 60 seconds
for _ in range(60):
    # Calculate total earnings per second

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
