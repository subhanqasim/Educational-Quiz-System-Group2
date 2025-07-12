import tkinter as tk

# Use style.py if available, otherwise fall back
try:
    from style import APP_FONT, BG_COLOR, BTN_COLOR, TEXT_COLOR
except ImportError:
    APP_FONT = ("Calibri", 13)
    BG_COLOR = "#CCCCFF"
    BTN_COLOR = "#9FE2BF"
    TEXT_COLOR = "#999999"

def info_screen(username,email, start_quiz_callback):
    win = tk.Toplevel()
    win.title("Quiz Instructions")
    win.geometry("500x350")
    win.configure(bg=BG_COLOR)

    instructions = (
        f"Welcome to the Quiz, {username}!\n\n"
        "Instructions:\n"
        "- The quiz has multiple-choice questions.\n"
        "- You have to select one option and click Next.\n"
        "- You will get your score at the end.\n"
        "- Try to answer all questions to the best of your knowledge.\n"
    )

    tk.Label(
        win,
        text=instructions,
        justify="left",
        wraplength=540,
        font=APP_FONT,
        bg=BG_COLOR,
        fg=TEXT_COLOR
    ).pack(pady=30)

    tk.Button(
        win,
        text="Start Quiz",
        command=lambda: [win.destroy(), start_quiz_callback(username,email)],
        bg=BTN_COLOR,
        fg="BLACK",
        font=("Arial", 12, "bold"),
        padx=15,
        pady=5
    ).pack(pady=10)
