import tkinter as tk
import time
import random

sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Typing speed is measured in words per minute.",
    "Python is a powerful programming language.",
    "Practice makes perfect when learning to code.",
    "Tkinter makes GUI development easy and fun."
]

class TypingTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("⌨️ Typing Speed Test")
        self.start_time = None
        self.target_text = random.choice(sentences)

        # UI Elements
        self.label = tk.Label(root, text="Type the sentence below:", font=("Arial", 14))
        self.label.pack(pady=10)

        self.sentence_display = tk.Label(root, text=self.target_text, wraplength=500, font=("Arial", 12), fg="blue")
        self.sentence_display.pack(pady=10)

        self.entry = tk.Text(root, height=5, width=60, font=("Arial", 12))
        self.entry.pack(pady=10)
        self.entry.bind("<KeyPress>", self.start_timer)

        self.result_label = tk.Label(root, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

        self.reset_btn = tk.Button(root, text="Reset", command=self.reset)
        self.reset_btn.pack(pady=5)

    def start_timer(self, event):
        if self.start_time is None:
            self.start_time = time.time()
        if event.keysym == "Return":
            self.calculate_speed()

    def calculate_speed(self):
        end_time = time.time()
        typed_text = self.entry.get("1.0", tk.END).strip()
        elapsed_time = end_time - self.start_time
        word_count = len(typed_text.split())
        wpm = round(word_count / (elapsed_time / 60), 2)

        # Accuracy
        correct_chars = sum(1 for i, j in zip(typed_text, self.target_text) if i == j)
        accuracy = round((correct_chars / len(self.target_text)) * 100, 2)

        self.result_label.config(text=f"⏱️ Time: {round(elapsed_time, 2)}s | 📝 WPM: {wpm} | 🎯 Accuracy: {accuracy}%")

    def reset(self):
        self.start_time = None
        self.target_text = random.choice(sentences)
        self.sentence_display.config(text=self.target_text)
        self.entry.delete("1.0", tk.END)
        self.result_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingTestApp(root)
    root.mainloop()