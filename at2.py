# Conversion factor: seconds per hour
seconds_per_hour = 3600

# Given lists
common = ['34', '.0000000011']
rare = ['22', '.0000000016']
epic = ['10', '.0000000022']
legendary = ['5', '.0000000044']

# Function to calculate earnings per hour
def calculate_earnings_per_hour(item):
    rate = float(item[0])  # Convert the rate to a float
    earnings_per_second = float(item[1])  # Convert earnings per second to a float
    earnings_per_hour = earnings_per_second * seconds_per_hour  # Convert earnings to per hour
    return rate * earnings_per_hour

# Calculate earnings per hour for each item
common_earnings_per_hour = calculate_earnings_per_hour(common)
rare_earnings_per_hour = calculate_earnings_per_hour(rare)
epic_earnings_per_hour = calculate_earnings_per_hour(epic)
legendary_earnings_per_hour = calculate_earnings_per_hour(legendary)

# Display the results
print(f"Common: {common_earnings_per_hour} per hour")
print(f"Rare: {rare_earnings_per_hour} per hour")
print(f"Epic: {epic_earnings_per_hour} per hour")
print(f"Legendary: {legendary_earnings_per_hour} per hour")
