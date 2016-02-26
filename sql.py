import sqlite3

with sqlite3.connect("library.db") as connection:
	c = connection.cursor()

	c.execute('''DROP TABLE books''')
	c.execute('CREATE TABLE books(title TEXT, author TEXT)')
	c.execute('INSERT INTO books VALUES("Harry Potter", "J.K.Rowling", )')
	c.execute('INSERT INTO books VALUES("Mastery", "Robert Green")')
	c.execute('INSERT INTO books VALUES("48 Laws of Power", "Robert Green",)')
	c.execute('INSERT INTO books VALUES("Art of Seduction", "Robert Green",)')
	c.execute('INSERT INTO books VALUES("Brain Dead", "John Saul", "Horror")')
	c.execute('INSERT INTO books VALUES("Carrie", "Stephen Kings", "Horror")')
	c.execute('INSERT INTO books VALUES("Harry Potter: Half Blood Prince", "J.K. Rowling")')
