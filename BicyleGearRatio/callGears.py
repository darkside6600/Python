import subprocess

stop = False

while not stop:
    print("1: Get gear ratios")
    print("2: Get gear inches")
    print("3: quit")
    choice = input("Enter your choice:")

    if choice == "1":
        subprocess.run(["python", "gear_ratio.py"])
    elif choice == "2":
        subprocess.run(["python", "gear_inches.py"])
    elif choice == "3":
        stop = True
