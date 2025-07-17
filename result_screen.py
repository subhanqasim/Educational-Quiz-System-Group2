import tkinter as tk

# Try importing styles; if not found, fallback to defaults
try:
    from style import APP_FONT, BG_COLOR, TEXT_COLOR
except ImportError:
    APP_FONT = ("Arial", 19)
    BG_COLOR = "#e0f7fa"
    TEXT_COLOR = "#004d40"

def result_screen(username, score, total):
    top = tk.Toplevel()
    top.title("Quiz Total Result ")
    top.geometry("500x250")
    top.configure(bg=BG_COLOR)

    tk.Label(
        top,
        text=f"Well done, {username}!",
        font=("Arial", 16, "bold"),
        bg=BG_COLOR,
        fg=TEXT_COLOR
    ).pack(pady=15)

    tk.Label(
        top,
        text=f"Your Score: {score} / {total}",
        font=("Arial", 14),
        bg=BG_COLOR,
        fg=TEXT_COLOR
    ).pack(pady=5)

    tk.Button(
        top,
        text="Exit",
        command=win.destroy,
        bg="#d32f2f",
        fg="white",
        font=("Arial", 12),
        padx=10,
        pady=5
    ).pack(pady=30)
