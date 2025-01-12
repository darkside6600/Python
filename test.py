dividends_per_share = 0.48
number_of_shares = 200
stock_price_per_share = 15.80

total_shares = number_of_shares

for month in range(1, 13):
    additional_shares = (dividends_per_share * total_shares) / stock_price_per_share
    total_shares += additional_shares

print(f"At the end of 12 months, you would own {total_shares:.2f} shares.")
