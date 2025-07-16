# Education Quiz System

## Project Overview
The Educational Quiz System is a Python Tkinter-based GUI application that lets users take multiple-choice quizzes with real-time scoring. It features user login, instructions, quiz interface, and result storage using SQLite. The project was collaboratively built using GitHub with feature branches, pull requests, and version control best practices.
---

## Team Members and Responsibilities

| Member        | Task                    | Branch Name           |
|---------------|-------------------------|-----------------------|
| Syed Ahmad Ali | Group Lead, Login, Database, Git Setup      | main, login, db    |
| Junaid          | Login Screen UI          | 	feature/login-screen  |
| Afifa      | Quiz Info Screen | feature/info-screen |
| Aneeqa | Result Screen            | feature/result-screen   |
| Abdullah| View Results Module        | feature/view-results    |

---

## How to Run
1-Make sure Python is installed on your system.
2-Open Terminal or Git Bash and navigate to the project folder using cd.
3-Run the app with python main.py or py main.py.
4-The login window will appear — sign up or log in to continue.
5-Follow on-screen instructions to take the quiz and view results.

---

## Project Structure
quiz_project/
├── main.py                  # Main entry point connecting all screens
├── login_screen.py          # User login and signup screen
├── info_screen.py           # Instructions screen before quiz starts
├── quiz_screen.py           # Quiz interface with questions
├── result_screen.py         # Displays user score after quiz
├── view_result.py           # Shows result history (admin or user)
├── database.py              # Handles SQLite database operations
├── style.py                 # Centralized styling (colors, fonts)
├── questions.json           # Quiz questions in JSON format
├── user_data.json           # Stores registered user credentials
├── quiz_results.db          # SQLite database storing quiz results
├── README.md                # Project documentation
└── __pycache__/             # Python cache (auto-generated)


---

## Contribution Guidelines
- Each member works on their assigned branch.
- Regularly push updates to your branch.
- Raise pull requests to merge features into the main branch after code review.

---

## Contact
For questions or feedback, contact the project leader:
*Syed Ahmad Ali*  
Email: syedahmadali152@gmail.com

---

✅ "Learn Smart. Play Sharp. Score High!"
