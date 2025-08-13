import tkinter as tk
from tkinter import messagebox
import random

# Game variables
random_number = random.randint(1, 100)
count = 0

def flash_message(message, color):
    """Flash the result label for visual feedback."""
    result_label.config(text=message, fg=color)
    root.update()
    result_label.after(150, lambda: result_label.config(fg="black"))
    result_label.after(300, lambda: result_label.config(fg=color))

def check_guess(event=None):  # event=None so it works with both button & Enter
    global count, random_number
    try:
        guess = int(entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid integer!")
        entry.delete(0, tk.END)
        return

    count += 1

    if guess < random_number:
        flash_message("Go Higher!", "blue")
    elif guess > random_number:
        flash_message("Go Lower!", "orange")
    else:
        messagebox.showinfo(
            "Congratulations",
            f"You got {random_number} correct in {count} attempts!"
        )
        reset_game()

    entry.delete(0, tk.END)

def reset_game():
    """Start a new game after a correct guess."""
    global random_number, count
    random_number = random.randint(1, 100)
    count = 0
    result_label.config(text="", fg="black")

# Main window
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("350x200")

title_label = tk.Label(root, text="Guess a number between 1 and 100", font=("Arial", 12))
title_label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=5)
entry.bind("<Return>", check_guess)  # Press Enter to guess

guess_button = tk.Button(root, text="Submit Guess", font=("Arial", 12), command=check_guess)
guess_button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
