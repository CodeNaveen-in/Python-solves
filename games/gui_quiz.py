import tkinter as tk
import requests
import html
import random

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🧠 Trivia Quiz")
        self.root.config(padx=30, pady=30, bg="#f0f4f8")

        self.score = 0
        self.question_index = 0
        self.questions = []
        self.selected_answer = tk.StringVar()

        self.title_label = tk.Label(text="🧠 Trivia Quiz", font=("Segoe UI", 24, "bold"), bg="#f0f4f8", fg="#333")
        self.title_label.pack(pady=(0, 20))

        self.question_label = tk.Label(text="", font=("Segoe UI", 16), wraplength=500, bg="#f0f4f8", justify="center")
        self.question_label.pack(pady=10)

        self.options_frame = tk.Frame(bg="#f0f4f8")
        self.options_frame.pack()

        self.radio_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(self.options_frame, text="", variable=self.selected_answer, value="", font=("Segoe UI", 14),
                                bg="#f0f4f8", anchor="w", justify="left")
            rb.pack(anchor="w", pady=5)
            self.radio_buttons.append(rb)

        self.submit_button = tk.Button(text="Submit", font=("Segoe UI", 12), bg="#4CAF50", fg="white", command=self.check_answer)
        self.submit_button.pack(pady=20)

        self.feedback_label = tk.Label(text="", font=("Segoe UI", 14), bg="#f0f4f8", fg="#333")
        self.feedback_label.pack()

        self.score_label = tk.Label(text="Score: 0", font=("Segoe UI", 12), bg="#f0f4f8", fg="#555")
        self.score_label.pack(pady=(10, 0))

        self.fetch_questions()

    def fetch_questions(self):
        url = "https://opentdb.com/api.php?amount=10&type=multiple"
        try:
            response = requests.get(url)
            data = response.json()
            self.questions = data["results"]
            self.load_question()
        except Exception as e:
            self.question_label.config(text="Failed to load questions. Check your internet connection.")
            print(f"Error: {e}")

    def load_question(self):
        if self.question_index < len(self.questions):
            q = self.questions[self.question_index]
            question_text = html.unescape(q["question"])
            correct = html.unescape(q["correct_answer"])
            incorrect = [html.unescape(ans) for ans in q["incorrect_answers"]]
            options = incorrect + [correct]
            random.shuffle(options)

            self.question_label.config(text=question_text)
            self.selected_answer.set(None)
            for i, opt in enumerate(options):
                self.radio_buttons[i].config(text=opt, value=opt)
        else:
            self.question_label.config(text="🎉 Quiz Completed!")
            self.submit_button.config(state="disabled")
            self.feedback_label.config(text=f"Final Score: {self.score}/10")

    def check_answer(self):
        selected = self.selected_answer.get()
        correct = html.unescape(self.questions[self.question_index]["correct_answer"])
        if selected == correct:
            self.score += 1
            self.feedback_label.config(text="✅ Correct!", fg="#4CAF50")
        else:
            self.feedback_label.config(text=f"❌ Incorrect! Correct answer: {correct}", fg="#F44336")

        self.score_label.config(text=f"Score: {self.score}")
        self.question_index += 1
        self.root.after(1500, self.load_question)

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()