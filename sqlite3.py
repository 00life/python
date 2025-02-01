import sqlite3

# create database
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# create table
cursor.execute('CREATE TABLE students (name text, age integer)')

# add data
cursor.execute('INSERT INTO students (name, age) VALUES (?, ?)', ('Jesse', 13))

# fetch all table
res = cursor.execute('SELECT * FROM students')
print(res.fetchall())

# fetch one
res = cursor.execute('SELECT * FROM students WHERE name = ?', ('Jesse',))
print(res.fetchone())

# close database 
conn.close()

#-------------------------

conn = sqlite3.connect('example.db')

conn.execute('''
CREATE TABLE users (
id INTEGER PRIMARY KEY,
name TEXT,
email TEXT
);
''')

conn.execute('''
INSERT INTO users (id, name, email)
VALUES (1, 'John Doe', 'john@example.com');
''')

conn.execute('''
INSERT INTO users (id, name, email)
VALUES (2, 'Jane Smith', 'jane@example.com');
''')

conn.execute('''
SELECT * FROM users;
''')

conn.execute('''
SELECT name, email FROM users;
''')

conn.execute('''
SELECT * FROM users
WHERE id = 1;
''')

conn.execute('''
SELECT * FROM users
ORDER BY name;
''')

conn.execute('''
SELECT * FROM users
LIMIT 2;
''')

# close database 
conn.close()