import sqlite3
conn = sqlite3.connect("database.db")
c = conn.cursor()
insert_statement = """INSERT INTO users (username, fname,lname,email,password,dateOfBirth) VALUES ("JBiden","Joe","Biden","Joever@gmail.com","Trumpsucks","20-11-1942");"""
c.execute(insert_statement)
insert_statement = """INSERT INTO users (username, fname,lname,email,password,dateOfBirth) VALUES ("DTrummp","Donald","Trump","MAGA@gmail.com","SleepyJoe","20-11-1942");"""
c.execute(insert_statement)
insert_statement = """INSERT INTO users (username, fname,lname,email,password,dateOfBirth) VALUES ("BoJo","Boris","Johnson","BoJo@gmail.com","CovidParties","19-6-1964");"""
c.execute(insert_statement)
insert_statement = """INSERT INTO movies (releaseDate,genre,movieName) VALUES ("27-12-1977","Science Fiction","Star Wars: A New Hope");"""
c.execute(insert_statement)
insert_statement = """INSERT INTO movies (releaseDate,genre,movieName) VALUES ("20-5-1980","Science Fiction","Star Wars: The Empire Strikes Back");"""
c.execute(insert_statement)
insert_statement = """INSERT INTO movies (releaseDate,genre,movieName) VALUES ("25-5-1983","Science Fiction","Star Wars: Return of the Jedi");"""
c.execute(insert_statement)
insert_statement = """INSERT INTO actor (stagename,fname,lname,age) VALUES (NULL,"Harrison","Ford",81);"""
c.execute(insert_statement)
conn.commit()
conn.close()