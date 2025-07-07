import sqlite3

def view_all_results():
    conn = sqlite3.connect("quiz_results.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM results ORDER BY timestamp DESC")
    results = cursor.fetchall()

    print("\n=== Quiz Results ===")
    for row in results:
        print(f"ID: {row[0]} | Name: {row[1]} | Email: {row[2]} | Score: {row[3]}/{row[4]} | Time: {row[5]}")

    conn.close()

if __name__ == "__main__":
    view_all_results()
