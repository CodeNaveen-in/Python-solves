import tkinter as tk
import random

# ---------------------------- DATA SETUP ------------------------------- #
flashcards = [
    {"French": "Bonjour", "English": "Hello"},
    {"French": "Merci", "English": "Thank you"},
    {"French": "Pomme", "English": "Apple"},
    {"French": "Chat", "English": "Cat"},
    {"French": "Chien", "English": "Dog"},
]

current_card = {}
flip_timer = None

# ---------------------------- CARD FLIP ------------------------------- #
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="#333")
    canvas.itemconfig(card_word, text=current_card["English"], fill="#333")
    canvas.config(bg="#f0f0f0")

# ---------------------------- NEXT CARD ------------------------------- #
def next_card():
    global current_card, flip_timer
    if flip_timer:
        window.after_cancel(flip_timer)
    current_card = random.choice(flashcards)
    canvas.itemconfig(card_title, text="French", fill="#3f51b5")
    canvas.itemconfig(card_word, text=current_card["French"], fill="#3f51b5")
    canvas.config(bg="#e3f2fd")
    flip_timer = window.after(3000, flip_card)

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Flashcard App")
window.config(padx=50, pady=50, bg="#ffffff")

canvas = tk.Canvas(width=400, height=250, bg="#e3f2fd", highlightthickness=0)
card_title = canvas.create_text(200, 80, text="", font=("Segoe UI", 24, "italic"))
card_word = canvas.create_text(200, 150, text="", font=("Segoe UI", 36, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
right_button = tk.Button(text="✅ Correct", width=12, font=("Segoe UI", 12), bg="#c8e6c9", command=next_card)
right_button.grid(row=1, column=1, pady=20)

wrong_button = tk.Button(text="❌ Wrong", width=12, font=("Segoe UI", 12), bg="#ffcdd2", command=next_card)
wrong_button.grid(row=1, column=0, pady=20)

next_card()
window.mainloop()