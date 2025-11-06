import tkinter as tk
import math

# ---------------------------- BASE TIMER LOGIC ------------------------------- #
class BaseTimer:
    WORK_MIN = 25
    SHORT_BREAK_MIN = 5
    LONG_BREAK_MIN = 20

    def __init__(self):
        self.timer = None
        self.paused = False
        self.remaining_time = 0

    def count_down(self, count):
        self.remaining_time = count
        minutes = math.floor(count / 60)
        seconds = count % 60
        if seconds < 10:
            seconds = f"0{seconds}"
        self.timer_label.config(text=f"{minutes}:{seconds}")
        if count > 0:
            self.timer = self.root.after(1000, self.count_down, count - 1)
        else:
            self.timer = None
            self.checkmarks.config(text="✔ Done!")

    def pause_resume(self):
        if self.timer:
            if not self.paused:
                self.root.after_cancel(self.timer)
                self.paused = True
                self.pause_button.config(text="Resume")
            else:
                self.paused = False
                self.pause_button.config(text="Pause")
                self.count_down(self.remaining_time)

    def reset_timer(self):
        if self.timer:
            self.root.after_cancel(self.timer)
            self.timer = None
        self.paused = False
        self.remaining_time = 0
        self.timer_label.config(text="00:00")
        self.title_label.config(text="🍅 Timer", fg="green")
        self.checkmarks.config(text="")
        self.pause_button.config(text="Pause")

    def start_timer(self):
        if self.timer:
            return
        self.paused = False
        mode = self.mode_var.get()
        if mode == "Work":
            self.remaining_time = self.WORK_MIN * 60
            self.title_label.config(text="💼 Work", fg="green")
        elif mode == "Short Break":
            self.remaining_time = self.SHORT_BREAK_MIN * 60
            self.title_label.config(text="☕ Short Break", fg="pink")
        elif mode == "Long Break":
            self.remaining_time = self.LONG_BREAK_MIN * 60
            self.title_label.config(text="🛌 Long Break", fg="red")
        self.count_down(self.remaining_time)

# ---------------------------- UI CLASS ------------------------------- #
class PomodoroUI(BaseTimer):
    def __init__(self, root):
        super().__init__()
        self.root = root
        self.root.title("Pomodoro Timer")
        self.root.config(padx=100, pady=50, bg="white")

        self.title_label = tk.Label(text="🍅 Timer", fg="green", bg="white", font=("Courier", 40))
        self.title_label.grid(column=1, row=0)

        self.timer_label = tk.Label(text="00:00", fg="black", bg="white", font=("Courier", 35, "bold"))
        self.timer_label.grid(column=1, row=1)

        self.mode_var = tk.StringVar(value="Work")
        self.mode_menu = tk.OptionMenu(root, self.mode_var, "Work", "Short Break", "Long Break")
        self.mode_menu.grid(column=1, row=2)

        self.start_button = tk.Button(text="Start", command=self.start_timer)
        self.start_button.grid(column=0, row=3)

        self.pause_button = tk.Button(text="Pause", command=self.pause_resume)
        self.pause_button.grid(column=1, row=3)

        self.reset_button = tk.Button(text="Reset", command=self.reset_timer)
        self.reset_button.grid(column=2, row=3)

        self.checkmarks = tk.Label(fg="green", bg="white", font=("Courier", 20))
        self.checkmarks.grid(column=1, row=4)

# ---------------------------- APP ENTRY POINT ------------------------------- #
class PomodoroApp(PomodoroUI):
    def __init__(self):
        root = tk.Tk()
        super().__init__(root)
        root.mainloop()

# Run the app
if __name__ == "__main__":
    PomodoroApp()