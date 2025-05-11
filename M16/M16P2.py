import tkinter as tk
from tkinter import messagebox
import os

# Load player data from file
def load_data():
    lastnames = []
    batting_averages = []
    with open("playerBA.txt", 'r') as file:
        for line in file:
            lastname, batting_average = line.strip().split('-')
            lastnames.append(lastname)
            batting_averages.append(float(batting_average))
    return lastnames, batting_averages

# Display player list in the text widget
def display_players(text_widget, lastnames, batting_averages):
    text_widget.insert(tk.END, "Lastnames and Batting Averages:\n")
    for i in range(len(lastnames)):
        text_widget.insert(tk.END, f"{lastnames[i]:<15} {batting_averages[i]:.3f}\n")

# Append a search result to the results file
def save_result_to_file(result_text):
    with open("search_results.txt", 'a') as file:  # 'a' mode creates file if it doesn't exist
        file.write(result_text + '\n')

# Search for a player and display result
def search_player():
    name = entry.get().strip()
    if not name:
        messagebox.showinfo("Input Error", "Please enter a last name.")
        return

    for i in range(len(lastnames)):
        if lastnames[i].lower() == name.lower():
            result_text = f"Found: {lastnames[i]} - {batting_averages[i]:.3f}"
            result_label.config(text=result_text)
            save_result_to_file(result_text)
            return

    result_text = f"{name} not found"
    result_label.config(text=result_text)
    save_result_to_file(result_text)

# Load data
lastnames, batting_averages = load_data()

# Create main window
root = tk.Tk()
root.title("Baseball Player Search")

# Text box to display player list
text_display = tk.Text(root, height=15, width=40)
text_display.pack(padx=10, pady=5)
display_players(text_display, lastnames, batting_averages)
text_display.config(state='disabled')  # prevent editing

# Entry box for user input
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# Button to trigger search
search_button = tk.Button(root, text="Search", command=search_player)
search_button.pack()

# Label to display search result
