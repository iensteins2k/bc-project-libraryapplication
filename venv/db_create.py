from librapp import db
from models import Libr 

#create database and the db tables
db.create_all()


# insert
db.session.add(Libr("iensteins", "iensteins@yahoo.com", "iensteins", 1, 200))
db.session.add(Libr("temi", "itemi@gmail.com", "temi", 2, 0))
db.session.add(Libr("ebuka", "ebuka@yahoo.com", "ebuka", 2, 0))
db.session.add(Libr("adims", "adims@yahoo.com", "adims", 1, 500))
db.session.add(Libr("chika", "chuka@yahoo.com", "chika", 1, 200))


#commit
db.session.commit()


	c.execute("""CREATE TABLE `users` (
	`_id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`username`	TEXT NOT NULL,
	`email`	TEXT NOT NULL,
	`password`	TEXT NOT NULL,
	`debtor`	INTEGER NOT NULL,
	`amount`	INTEGER NOT NULL,
	`avatar`	BLOB NOT NULL
)""")
	c.execute("""CREATE TABLE `borrow` (
	`_id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`users_id`	TEXT NOT NULL,
	`books_id`	TEXT NOT NULL,
	`debtor`	INTEGER NOT NULL,
	`amount`	INTEGER NOT NULL,
	`avatar`	BLOB NOT NULL
)""")