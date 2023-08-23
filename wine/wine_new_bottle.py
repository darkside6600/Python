''''
this is for entering in a new bottle of wine.

Year, Wine maker, type
'''
import colorama, csv, os

colorama.init()

wine_file = ".\wine_collection.csv"
print("\033[2J\033[1;1f")
wine_collection = []
def inputWine(wine_collection):

    year = input("Enter the year of the wine: ")
    manufacturer = input("Enter the manufacturer of the wine: ")
    wine_type = input("Enter the type of the wine: ")

    wine = {
        "Year": year,
        "Manufacturer": manufacturer,
        "Type": wine_type
    }

    wine_collection.append(wine)

    print("Wine added successfully!")

def write_list_to_csv(data_list, file_name):
    file_exists = os.path.isfile(file_name) # check if file exists   
    with open(file_name, 'a' if file_exists else 'w', newline='') as csvfile:    
        csv_writer = csv.writer(csvfile)
        if not file_exists:
            csv_writer.writerow(["Year", "Manufacturer", "Type"])  # Write header row
        for row in data_list:
            csv_writer.writerow([row["Year"], row["Manufacturer"], row["Type"]])

def main():
    while True:
        newBottle = input("Enter in a new bottle (y/n)?  ")
        if newBottle.lower() == "n":
            break
        else:
            inputWine(wine_collection)
    print(wine_collection)
    write_list_to_csv(wine_collection, wine_file)  # Write to CSV file

if __name__ == "__main__":
    main()