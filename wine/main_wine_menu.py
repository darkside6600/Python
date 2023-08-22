import subprocess


def displayMenu(menu):
    print("Wine Menu:")
    for key, value in menu.items():
        print(f"{key}. {value}")

def main():
    menu = {
        1: "List all wines",
        2: "List all Red wines",
        3: "List all White wines",
        4: "List all other wines",
        5: "Enter in a new bottle of wine",
        6: "Delete a  bottle of wine",
        7: "Exit"
    }

    while True:
        displayMenu(menu)
        choice = input("Please make a selection: ")

        if choice.isdigit():
            choice = int(choice)
            if choice in menu:
                if choice == 1:
                    subprocess.run(["python", "wine_list.py"])
                if choice == 5:
                    subprocess.run(["python", "wine_new_bottle.py"])
                if choice == 7:
                    print("Quiting")
                    break
                elif choice > 7:
                    print("Invalid input.  Please enter a number between 1-7.")
                else:
                    print(f"your selected: {menu[choice]}")
        else:
            print("Invalid input.  Please enter a number between 1-7.")
    
if __name__ == "__main__":
    main()
