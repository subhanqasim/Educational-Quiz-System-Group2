import sqlite3

def view_all_results():
    try:
        conn = sqlite3.connect("quiz_results.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM results ORDER BY timestamp DESC")
        results = cursor.fetchall()

        print("\n=== Quiz Results ===")
        if not results:
            print("No results found.")
        else:
            print("{:<5} {:<15} {:<25} {:<10} {:<20}".format("ID", "Name", "Email", "Score", "Time"))
            print("-" * 80)
            for row in results:
                print("{:<5} {:<15} {:<25} {}/{} {:<20}".format(row[0], row[1], row[2], row[3], row[4], row[5]))

    except sqlite3.Error as e:
        print("Database error:", e)

    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    view_all_results()
