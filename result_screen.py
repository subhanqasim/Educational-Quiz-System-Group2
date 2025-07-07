import tkinter as tk

# Try importing styles; if not found, fallback to defaults
try:
    from style import APP_FONT, BG_COLOR, TEXT_COLOR
except ImportError:
    APP_FONT = ("Arial", 19)
    BG_COLOR = "#e0f7fa"
    TEXT_COLOR = "#004d40"

def result_screen(username, score, total):
    win = tk.Toplevel()
    win.title("Quiz Total Result ")
    win.geometry("500x250")
    win.configure(bg=BG_COLOR)

    tk.Label(
        win,
        text=f"Well done, {username}!",
        font=("Arial", 16, "bold"),
        bg=BG_COLOR,
        fg=TEXT_COLOR
    ).pack(pady=15)

    tk.Label(
        win,
        text=f"Your Score: {score} / {total}",
        font=("Arial", 14),
        bg=BG_COLOR,
        fg=TEXT_COLOR
    ).pack(pady=5)

    tk.Button(
        win,
        text="Exit",
        command=win.destroy,
        bg="#d32f2f",
        fg="white",
        font=("Arial", 12),
        padx=10,
        pady=5
    ).pack(pady=30)
