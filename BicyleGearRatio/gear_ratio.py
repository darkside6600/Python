import os
import file_writer


def ratio(front, rear):
    gearRatio = []
    for r in rear:
        gr = round(int(front)/int(r), 2)
        gearRatio.append(gr)
    return (gearRatio)


def rings():
    front = input("Enter in front chain ring:")
    rear = input("Enter in rear cassette values sperated by a comma:")
    rear = rear.split(",")
    return front, rear


chainring, cassette = rings()
gearRatio = ratio(chainring, cassette)
print(gearRatio)


filename = "gear_ratio.txt"
filewrite = "with a chain ring of " + chainring + "and a cassett of  " + cassette + " you get the following gear ratio" + gearRatio
# Check if the file exists
if os.path.isfile(filename):
    print("File already exists.")
else:
    # Open the file in write mode
    with open(filename, "w") as file:
        # Write the variables to the file
        file.write(filewrite + "\n")
    print("Variables written to the file.")