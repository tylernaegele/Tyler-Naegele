import tkinter as tk
from tkinter import messagebox

def load_data():
    lastnames = []
    batting_averages = []
    with open("playerBA.txt", 'r') as file:
        for line in file:
            lastname, batting_average = line.strip().split('-')
            lastnames.append(lastname)
            batting_averages.append(float(batting_average))
    return lastnames, batting_averages

def display_players(text_widget, lastnames, batting_averages):
    text_widget.insert(tk.END, "Lastnames and Batting Averages:\n")
    for i in range(len(lastnames)):
        text_widget.insert(tk.END, f"{lastnames[i]:<15} {batting_averages[i]:.3f}\n")

def search_player():
    name = entry.get().strip()
    if not name:
        messagebox.showinfo("Input Error", "Please enter a last name.")
        return
    for i in range(len(lastnames)):
        if lastnames[i].lower() == name.lower():
            result_label.config(text=f"Found: {lastnames[i]} - {batting_averages[i]:.3f}")
            return
    result_label.config(text="Name not found")

# Load data
lastnames, batting_averages = load_data()

# Create main window
root = tk.Tk()
root.title("Baseball Player Search")

# Display list
text_display = tk.Text(root, height=15, width=40)
text_display.pack(padx=10, pady=5)
display_players(text_display, lastnames, batting_averages)
text_display.config(state='disabled')

# Search area
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

search_button = tk.Button(root, text="Search", command=search_player)
search_button.pack()

result_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
result_label.pack(pady=5)

root.mainloop()