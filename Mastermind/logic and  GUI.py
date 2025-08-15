import tkinter as tk
from tkinter import messagebox
import random

colours = ["Y", "B", "R", "G", "P", "O", "V"]
colour_map = {
    "Y": ("Yellow", "#FFFF00"),
    "B": ("Blue", "#0000FF"),
    "R": ("Red", "#FF0000"),
    "G": ("Green", "#008000"),
    "P": ("Purple", "#800080"),
    "O": ("Orange", "#FFA500"),
    "V": ("Violet", "#EE82EE")
}

def start_new_game():
    global sequence, level, score
    level = 1
    score = 0
    lbl_score.config(text=f"Score: {score}")
    generate_sequence()
    show_sequence()

def generate_sequence():
    global sequence
    sequence = random.choices(colours, k=level)

def show_sequence():
    disable_inputs()
    for widget in sequence_frame.winfo_children():
        widget.destroy()
    for col in sequence:
        tk.Label(sequence_frame, width=8, height=3, bg=colour_map[col][1], relief="ridge").pack(side="left", padx=5)
    root.after(3000, hide_sequence)

def hide_sequence():
    for widget in sequence_frame.winfo_children():
        widget.destroy()
    enable_inputs()

def check_guess():
    guess = [var.get() for var in vars_list[:level]]
    if guess == sequence:
        next_level()
    else:
        messagebox.showinfo("Game Over", f"Wrong! Final Score: {score}")
        start_new_game()

def next_level():
    global level, score
    score += 10
    level += 1
    lbl_score.config(text=f"Score: {score}")
    for v in vars_list:
        v.set("")
    generate_sequence()
    show_sequence()

def disable_inputs():
    for menu in dropdowns:
        menu.config(state="disabled")
    btn_check.config(state="disabled")

def enable_inputs():
    for menu in dropdowns[:level]:
        menu.config(state="normal")
    btn_check.config(state="normal")

root = tk.Tk()
root.title("Memory Colour Game")
root.geometry("500x350")

tk.Label(root, text="Memorize the sequence!", font=("Arial", 14, "bold")).pack(pady=10)
lbl_score = tk.Label(root, text="Score: 0", font=("Arial", 12))
lbl_score.pack()

sequence_frame = tk.Frame(root)
sequence_frame.pack(pady=10)

vars_list = [tk.StringVar() for _ in range(8)]
for v in vars_list:
    v.set("")
opts = [""] + colours
dd_frame = tk.Frame(root)
dd_frame.pack(pady=10)
dropdowns = []
for var in vars_list:
    menu = tk.OptionMenu(dd_frame, var, *opts)
    menu.config(state="disabled")
    menu.pack(side="left", padx=5)
    dropdowns.append(menu)

btn_check = tk.Button(root, text="Check Guess", command=check_guess, bg="lightgreen")
btn_check.pack(pady=15)

start_new_game()
root.mainloop()
