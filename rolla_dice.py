import tkinter as tk
import random

# Function to roll the dice
def roll_dice():
    dice_number = random.randint(1, 6)
    dice_label.config(text=f"You rolled: {dice_number}", font=("Arial", 18))

# Set up the main window
window = tk.Tk()
window.title("Dice Rolling Simulator") 
window.geometry("300x200")
window.configure(bg="#f0f0f0")

# Title
title = tk.Label(window, text="Dice Rolling Simulator", font=("Arial", 16, "bold"), bg="#f0f0f0")
title.pack(pady=10)

# Label to show result
dice_label = tk.Label(window, text="🎲 Roll the dice!", font=("Arial", 14), bg="#f0f0f0")
dice_label.pack(pady=20)

# Roll Button
roll_button = tk.Button(window, text="Roll Dice", command=roll_dice, font=("Arial", 12), bg="#4CAF50", fg="white", padx=10, pady=5)
roll_button.pack()

# Run the application
window.mainloop()
