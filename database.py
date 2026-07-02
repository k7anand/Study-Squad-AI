import sqlite3
from pathlib import Path

# Always use the database in the project root
database_name = Path(__file__).resolve().parent / "study_squad.db"



def get_connection():
    """Return a connection to the SQLite database."""
    return sqlite3.connect(database_name)



def initialize_database():
    """Create the quiz_results table if it does not exist."""

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS quiz_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject TEXT NOT NULL,
            topic TEXT NOT NULL,
            score REAL NOT NULL
        )
    """)

    connection.commit()
    connection.close()



def insert_quiz_result(subject: str, topic: str, score: float):
    """Insert a quiz result into the database."""

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO quiz_results (subject, topic, score)
        VALUES (?, ?, ?)
    """, (subject, topic, score))

    connection.commit()
    connection.close()



def get_all_quiz_results():
    """Return every quiz result."""

    connection = get_connection()
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM quiz_results
        ORDER BY id
    """)

    rows = cursor.fetchall()
    connection.close()

    return [dict(row) for row in rows]



def get_weak_topics(threshold: float = 70):
    """Return quiz results below the threshold."""

    connection = get_connection()
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute("""
        SELECT subject, topic, score
        FROM quiz_results
        WHERE score < ?
        ORDER BY score ASC
    """, (threshold,))

    rows = cursor.fetchall()
    connection.close()

    return [dict(row) for row in rows]



def clear_database():
    """Delete all quiz history."""

    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM quiz_results")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='quiz_results'")
    connection.commit()
    connection.close()



if __name__ == "__main__":
    initialize_database()
    print("Database has been initialized!")
