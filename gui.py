import tkinter as tk

def save_text():
    user_input = text_entry.get()
    with open("D:\\git\\Python\\work\\user_input.txt", "w") as file:
        file.write(user_input)
    print("Text saved to D:\\git\\Python\\work\\user_input.txt")

# Create the main window
root = tk.Tk()
root.title("Who built me plus inventory")


# Create a label and text entry widget on the same line using grid
alias = tk.Label(root, text="Enter your alias:")
alias.grid(row=0, column=0, padx=5, pady=10)

text_entry = tk.Entry(root)
text_entry.grid(row=0, column=1, padx=5, pady=10)


# new label
ticket = tk.Label(root, text="Enter ticket number:")
ticket.grid(row=1, column=0, padx=5, pady=10)
ticket_entry = tk.Entry(root)
ticket_entry.grid(row=1, column=1, padx=5, pady=10)
# Create a button that will call the save_text function
button = tk.Button(root, text="Submit", command=save_text)
button.grid(row=5, column=1, padx=5, pady=15)

# Run the main loop
root.mainloop()
