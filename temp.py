unit = input ("Is this tempature in C or F: ")
temp = float(input ("Enter in the tempature: "))

if unit == "f":
    temp = temp / 32
    print (f"The temp is {temp} degrees C")
elif unit == "c":
    temp = temp * 2 + 32
    print (f"The temp is {temp} degrees F")
else:
    print (f"the {unit} was invalid")
    