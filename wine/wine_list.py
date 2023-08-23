'''
This wil list out all wines 
'''
import msvcrt
import colorama, csv
import pandas as pd

colorama.init()


print("\033[2J\033[1;1f")
'''
wine_collection = []


def read_csv_file(wine_file):
    data_list = []
    with open(wine_file, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        header = next(csv_reader)  # Read the header row
        for row in csv_reader:
            data_list.append(row)
    return data_list

def main():
    wine_file = ".\wine_collection.csv"
    wine_data = read_csv_file(wine_file)
    
    for row in wine_data:
        print(row)
'''
def main():
    file = "wine_collection.csv"
    df = pd.read_csv(file)
    pd.options.display.max_columns = len(df.columns)
    print(df)
    while True:
        print("Press any key to continue.")
        key = msvcrt.getch()  # For Windows
        if key:
            break

if __name__ == "__main__":
    main()
