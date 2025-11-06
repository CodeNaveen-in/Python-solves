import tkinter as tk
import math

# ---------------------------- CONSTANTS ------------------------------- #
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = None
paused = False
remaining_time = 0

# ---------------------------- TIMER CONTROL ------------------------------- #
def reset_timer():
    global timer, paused, remaining_time
    if timer:
        window.after_cancel(timer)
        timer = None
    paused = False
    remaining_time = 0
    timer_label.config(text="00:00")
    title_label.config(text="🍅 Timer", fg=ACCENT_COLOR)
    checkmarks.config(text="")
    pause_button.config(text="Pause")

def start_timer():
    global timer, remaining_time, paused
    if timer:
        return
    paused = False
    mode = mode_var.get()
    if mode == "Work":
        remaining_time = WORK_MIN * 60
        title_label.config(text="💼 Work", fg="#4CAF50")
    elif mode == "Short Break":
        remaining_time = SHORT_BREAK_MIN * 60
        title_label.config(text="☕ Short Break", fg="#FF9800")
    elif mode == "Long Break":
        remaining_time = LONG_BREAK_MIN * 60
        title_label.config(text="🛌 Long Break", fg="#F44336")
    count_down(remaining_time)

def pause_resume_timer():
    global paused, timer
    if timer:
        if not paused:
            window.after_cancel(timer)
            paused = True
            pause_button.config(text="Resume")
        else:
            paused = False
            pause_button.config(text="Pause")
            count_down(remaining_time)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer, remaining_time
    remaining_time = count
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    timer_label.config(text=f"{minutes}:{seconds}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        timer = None
        checkmarks.config(text="✔ Done!")

# ---------------------------- UI SETUP ------------------------------- #
BG_COLOR = "#f0f4f8"
ACCENT_COLOR = "#3f51b5"
FONT_NAME = "Segoe UI"

window = tk.Tk()
window.title("Pomodoro Timer")
window.config(padx=40, pady=40, bg=BG_COLOR)

# Title
title_label = tk.Label(
    text="🍅 Timer",
    fg=ACCENT_COLOR,
    bg=BG_COLOR,
    font=(FONT_NAME, 36, "bold")
)
title_label.grid(column=1, row=0, pady=(0, 20))

# Timer display
timer_label = tk.Label(
    text="00:00",
    fg="#212121",
    bg=BG_COLOR,
    font=(FONT_NAME, 40, "bold")
)
timer_label.grid(column=1, row=1, pady=10)

# Mode selector
mode_var = tk.StringVar(value="Work")
mode_menu = tk.OptionMenu(window, mode_var, "Work", "Short Break", "Long Break")
mode_menu.config(font=(FONT_NAME, 12), bg="white", fg="#333", width=15)
mode_menu.grid(column=1, row=2, pady=10)

# Buttons
button_style = {"font": (FONT_NAME, 12), "bg": "#e0e0e0", "fg": "#333", "width": 10, "bd": 0, "relief": "ridge"}

start_button = tk.Button(text="Start", command=start_timer, **button_style)
start_button.grid(column=0, row=3, padx=5, pady=10)

pause_button = tk.Button(text="Pause", command=pause_resume_timer, **button_style)
pause_button.grid(column=1, row=3, padx=5, pady=10)

reset_button = tk.Button(text="Reset", command=reset_timer, **button_style)
reset_button.grid(column=2, row=3, padx=5, pady=10)

# Checkmarks
checkmarks = tk.Label(fg="#4CAF50", bg=BG_COLOR, font=(FONT_NAME, 20))
checkmarks.grid(column=1, row=4, pady=10)

window.mainloop()