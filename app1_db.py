# app1_db.py(todo_db)
import sqlite3

# DB接続（なければ作成）
conn = sqlite3.connect("todo.db")
cursor = conn.cursor()

# テーブル作成
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    done BOOLEAN NOT NULL DEFAULT 0
    )
"""
)

# タスク追加
cursor.execute("INSERT INTO tasks (title, done) VALUES (?, ?)", ("Buy milk", 0))

# タスク取得
cursor.execute("SELECT * FROM tasks")
for row in cursor.fetchall():
    print(row)

conn.commit()
conn.close()

# print("Hello from todo_db")
