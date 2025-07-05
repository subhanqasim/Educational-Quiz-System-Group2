
import tkinter as tk
from tkinter import messagebox
import json
import re

# Try to import style or fall back
try:
    from style import APP_FONT, BG_COLOR, BTN_COLOR, TEXT_COLOR
except ImportError:
    APP_FONT = ("Arial", 12)
    BG_COLOR = "#e3f2fd"
    BTN_COLOR = "#1e88e5"
    TEXT_COLOR = "#0d47a1"

USER_DATA_FILE = "user_data.json"

def read_user_data():
    try:
        with open(USER_DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def write_user_data(data):
    with open(USER_DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def validate_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def login_screen(start_quiz_callback):
    window = tk.Tk()
    window.title("Login")
    window.geometry("350x350")
    window.configure(bg=BG_COLOR)

    tk.Label(window, text="Email", font=APP_FONT, bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=10)
    email_entry = tk.Entry(window, font=APP_FONT)
    email_entry.pack()

    tk.Label(window, text="Password", font=APP_FONT, bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=10)
    password_entry = tk.Entry(window, show="*", font=APP_FONT)
    password_entry.pack()

    def proceed():
        email = email_entry.get().strip()
        password = password_entry.get().strip()
        users = read_user_data()
        if email in users and users[email]["password"] == password:
            window.destroy()
            start_quiz_callback(users[email]["name"], email)
        else:
            messagebox.showwarning("Login Error", "Invalid email or password")

    tk.Button(window, text="Login", command=proceed, bg=BTN_COLOR, fg="white", font=APP_FONT).pack(pady=20)
    tk.Button(window, text="Sign Up", command=lambda: signup_screen(window, start_quiz_callback), bg="#ff9800", fg="white", font=APP_FONT).pack(pady=5)
    window.mainloop()

def signup_screen(login_window, start_quiz_callback):
    signup_window = tk.Toplevel()
    signup_window.title("Sign Up")
    signup_window.geometry("350x400")
    signup_window.configure(bg=BG_COLOR)

    tk.Label(signup_window, text="Name", font=APP_FONT, bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=10)
    name_entry = tk.Entry(signup_window, font=APP_FONT)
    name_entry.pack()

    tk.Label(signup_window, text="Email", font=APP_FONT, bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=10)
    email_entry = tk.Entry(signup_window, font=APP_FONT)
    email_entry.pack()

    tk.Label(signup_window, text="Password", font=APP_FONT, bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=10)
    password_entry = tk.Entry(signup_window, show="*", font=APP_FONT)
    password_entry.pack()

    def submit_signup():
        name = name_entry.get().strip()
        email = email_entry.get().strip()
        password = password_entry.get().strip()

        if not name or not email or not password:
            messagebox.showwarning("Input Error", "Please fill in all fields")
        elif not validate_email(email):
            messagebox.showwarning("Invalid Email", "Please enter a valid email address")
        elif len(password) < 6:
            messagebox.showwarning("Weak Password", "Password must be at least 6 characters")
        else:
            users = read_user_data()
            if email in users:
                messagebox.showwarning("Already Registered", "This email is already registered")
            else:
                users[email] = {"name": name, "password": password}
                write_user_data(users)
                messagebox.showinfo("Success", "You have registered successfully!")
                signup_window.destroy()
                login_window.deiconify()

    tk.Button(signup_window, text="Sign Up", command=submit_signup, bg=BTN_COLOR, fg="white", font=APP_FONT).pack(pady=20)