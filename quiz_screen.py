import tkinter as tk
import json
from database import save_result

try:
    from style import APP_FONT, BG_COLOR, BTN_COLOR, TEXT_COLOR
except ImportError:
    APP_FONT = ("Arial", 14)
    BG_COLOR = "#f0f0f0"
    BTN_COLOR = "#4CAF50"
    TEXT_COLOR = "#212121"

class Quiz:
    def __init__(self, username, email, show_result_callback):
        print("[DEBUG] Quiz screen initialized")
        self.username = username
        self.email = email
        self.show_result_callback = show_result_callback
        self.window = tk.Toplevel()
        self.window.title("Quiz")
        self.window.geometry("600x400")
        self.window.configure(bg=BG_COLOR)

        try:
            with open("questions.json") as f:
                self.questions = json.load(f)
        except Exception as e:
            print(f"[ERROR] Cannot load questions.json: {e}")
            self.questions = []

        if not self.questions:
            tk.Label(
                self.window,
                text="No questions found.",
                fg="red",
                bg=BG_COLOR,
                font=APP_FONT
            ).pack(pady=20)
            return

        self.q_index = 0
        self.score = 0
        self.var = tk.StringVar()
        self.load_question()

    def load_question(self):
        for widget in self.window.winfo_children():
            widget.destroy()

        q = self.questions[self.q_index]
        tk.Label(
            self.window,
            text=f"Q{self.q_index + 1}: {q['question']}",
            bg=BG_COLOR,
            fg=TEXT_COLOR,
            font=("Arial", 14, "bold")
        ).pack(pady=10)

        self.var.set(None)
        for opt in q['options']:
            tk.Radiobutton(
                self.window,
                text=opt,
                variable=self.var,
                value=opt,
                font=APP_FONT,
                bg=BG_COLOR,
                fg=TEXT_COLOR,
                selectcolor=BTN_COLOR,
                anchor="w",
                justify="left"
            ).pack(anchor='w', padx=30, pady=2)

        tk.Button(
            self.window,
            text="Next",
            command=self.next_question,
            bg=BTN_COLOR,
            fg="white",
            font=("Arial", 12),
            padx=10,
            pady=5
        ).pack(pady=20)

    def next_question(self):
        selected = self.var.get()
        if selected == self.questions[self.q_index]['answer']:
            self.score += 1
        self.q_index += 1
        if self.q_index < len(self.questions):
            self.load_question()
        else:
            self.window.destroy()
            save_result(self.username, self.email, self.score, len(self.questions))
            self.show_result_callback(self.username, self.score, len(self.questions))
