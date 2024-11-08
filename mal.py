import sqlite3
import os

# Path to Chrome's cookies file
cookies_file = os.path.join(os.path.expanduser("~"), "AppData", "Local", "Google", "Chrome", "User Data", "Default", "Cookies")

# Connect to the SQLite database
con = sqlite3.connect(cookies_file)
cur = con.cursor()

# Query the cookies table
cur.execute("SELECT * FROM cookies")

# Fetch and print the cookies
rows = cur.fetchall()
for row in rows:
    print(row)

# Close the connection
con.close()
