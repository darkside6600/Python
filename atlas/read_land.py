import csv


def getLandList():
    land_file = "atlas\LandOwned.csv"
    land_list = []  # Renamed variable to avoid conflict
    with open(land_file, mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            land_list.append(row)
    return land_list


list = getLandList()
for item in list:
    print (item)
