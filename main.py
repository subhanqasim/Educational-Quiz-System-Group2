from database import init_db
init_db()  # Create DB table if not exists

from login_screen import login_screen
from quiz_screen import Quiz
from result_screen import result_screen
from info_screen import info_screen

# Called after login screen
def start_info(username, email):
    print(f"[DEBUG] Received from login: {username} ({email})")
    info_screen(username, email, start_quiz)

# Called after info screen
def start_quiz(username, email):
    print(f"[DEBUG] Received from info screen: {username} ({email})")
    Quiz(username, email, result_screen)

if __name__ == '__main__':
    print("[DEBUG] Application started")
    login_screen(start_info)
