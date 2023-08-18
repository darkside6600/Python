def Ratio():
    
    front = input("Enter in front chain ring:")
    rear = input("Enter in rear cassette values sperated by a comma:")
    rear = rear.split(",")
    gearRatio = []
    for r in rear:
        gr = round(int(front)/int(r), 2)
        gearRatio.append(gr)
    print(gearRatio)
    oldGearRatio = gearRatio



def Inches():
    wheel = 26.8
    gearInch = []
    front = input("Enter front chain ring:")
    rear = input("Enter in rear cassette values seperated by a comma:")
    rear = rear.split(",")
    for r in rear:
        gi = round(wheel * (int(front)/int(r)), 2)
        gearInch.append(gi)
    print(gearInch)


stop = False

while (stop is False):
    print("Let's determine gear ratio and gear inches")
    print("1: Select 1 to show gear ratios")
    print("2: Select 2 to show gear inches")
    print("3: Select 3 to quit")
    go_or_stop = input("Enter choice:")
    if go_or_stop == "1":
        Ratio()
    elif go_or_stop == "2":
        Inches()
    else:
        stop = True
