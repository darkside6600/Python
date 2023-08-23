import subprocess
import colorama
colorama.init()

def displayMenu(menu):
    print("\033[2J\033[1;1f")
    print("Wine Menu:")
    for key, value in menu.items():
        print(f"{key}. {value}")

def main():
    print("\033[2J\033[1;1f")
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
                if choice == 2:
                    subprocess.run(["python", "wine_red_list.py"])
                if choice == 3:
                    subprocess.run(["python", "wine_white_list.py"])
                if choice == 4:
                    subprocess.run(["python", "wine_other_list.py"])
                if choice == 5:
                    subprocess.run(["python", "wine_new_bottle.py"])
                if choice == 6:
                    subprocess.run(["python", "wine_delete_bottle.py"])
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
