''''
this will list all wines that are reds
Syrah, merlot, Cabernet Sauvignon, Malbec, Pnot Noir
Zinfandel, Sangiovese, Barbera
'''
import msvcrt
import csv
import pandas as pd
import colorama
colorama.init()

print("\033[2J\033[1;1f")
def listRed(wine_data):
    listingOfReds = []
    redWines = ["Syrah", "merlot", "Cabernet Sauvignon", "Malbec", "Pnot Noir", "Zinfandel", "Sangiovese", "Barbera"]
    for wine in wine_data:
        winetype = wine[2]
        if winetype in redWines:
            listingOfReds.append(wine)

    return listingOfReds


def getWineList():
    wine_file = "wine_collection.csv"
    wine_list = []  # Renamed variable to avoid conflict
    with open(wine_file, mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            wine_list.append(row)
    return wine_list

def main():
    wine_data = getWineList()
    reds = listRed(wine_data)
    if reds:
        df = pd.DataFrame(reds, columns=["Year", "Winery", "Type", "Quantity"])
        print(df)
    else:
        print("No red wines found in the collection.")

    while True:
        print("Press any key to continue.")
        key = msvcrt.getch()  # For Windows
        if key:
            break

if __name__ == "__main__":
    main()
