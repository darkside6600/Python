''''
this will list all wines that are white
Chardonnay, Riesling, Sauvignon Blanc, Semillon
Moscato, Pino Grigio, Gewurztraminer, Chenin Blanc
Viognier Verdelho
'''

import msvcrt, colorama, csv
import pandas as pd
colorama.init()

print("\033[2J\033[1;1f")

def listWhite(wine_data):
    listingOfWhites = []
    whiteWines = ["Chardonnay", "Riesling", "Sauvignon Blanc", "Semillon","Moscato", "Pino Grigio", "Gewurztraminer", "Chenin Blanc","Viognier Verdelho"]
    for wine in wine_data:
        winetype = wine[2]
        if winetype in whiteWines:
            listingOfWhites.append(wine)

    return listingOfWhites


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
    whites = listWhite (wine_data)
    white_list = pd.Series(whites)
    print(white_list)
    while True:
        print("Press any key to continue.")
        key = msvcrt.getch()  # For Windows
        if key:
            break

if __name__ == "__main__":
    main()
