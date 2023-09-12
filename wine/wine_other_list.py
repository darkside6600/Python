''''
this will list all wines that are neither white or red
'''


import msvcrt, colorama, csv
import pandas as pd
colorama.init()

print("\033[2J\033[1;1f")

def listOther(wine_data):
    listingOfOthers = []
    otherWines = ["Chardonnay", "Riesling", "Sauvignon Blanc", "Semillon","Moscato", "Pinot Grigio", "Gewurztraminer", "Chenin Blanc",
                  "Viognier Verdelho", "Syrah", "Merlot", "Cabernet Sauvignon", "Malbec", "Pinot Noir", "Zinfandel", "Sangiovese", "Barbera"]
    for wine in wine_data:
        winetype = wine[2]
        if winetype not in otherWines:
            listingOfOthers.append(wine)

    return listingOfOthers


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
    others = listOther(wine_data)
    if others:
        df = pd.DataFrame(others, columns=["Year", "Winery", "Type", "Quantity"])
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
