import sqlite3
connection = sqlite3.connect('needles.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO needles (title, content) VALUES (?, ?)",
            ('First Needle', 'Content for the first needle')
            )
cur.execute("Insert INTO needles (title, content) VALUES (?, ?)",
            ('Second Needle', 'Content for the second needle')
            )

connection.commit()
connection.close()