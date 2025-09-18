from database import get_db

conn = get_db()
cursor = conn.cursor()

# See what’s in the expenses table
cursor.execute("SELECT * FROM expenses")
rows = cursor.fetchall()

print("Expenses in DB:")
for row in rows:
    print(dict(row))  # convert Row object to dictionary for readability

conn.close()
