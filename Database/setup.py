import sqlite3
# create .db file or connect to it if it exists
conn = sqlite3.connect("database.db")
# A cursor is an object used to make the connection for executing SQL queries.
c = conn.cursor()
# Create the table, read the article below if you
# are unsure of what VARCHAR etc. mean
# https://www.w3schools.com/sql/sql_datatypes.asp
create_table_statement = """CREATE TABLE IF NOT EXISTS users (
  userID INTEGER PRIMARY KEY,
  username VARCHAR(255),
  fname VARCHAR(30),
  lname VARCHAR(30),
  email VARCHAR(255),
  password VARCHAR(255),
  dateOfBirth DATE
);"""
c.execute(create_table_statement)
create_table_statement = """CREATE TABLE IF NOT EXISTS movies (
  movieID INTEGER PRIMARY KEY,
  releaseDate Date,
  genre VARCHAR(30),
  movieName VARCHAR(255)
);"""
c.execute(create_table_statement)
create_table_statement = """CREATE TABLE IF NOT EXISTS review (
  reviewID INTEGER PRIMARY KEY,
  userID INTEGER,
  movieID INTEGER,
  score FLOAT
);"""
c.execute(create_table_statement)
create_table_statement = """CREATE TABLE IF NOT EXISTS actor (
  actorID INTEGER PRIMARY KEY,
  stagename VARCHAR(30),
  fname VARCHAR(30),
  lname VARCHAR(30),
  age INTEGER
);"""
c.execute(create_table_statement)
create_table_statement = """CREATE TABLE IF NOT EXISTS actorRole (
  ActorRole INTEGER PRIMARY KEY,
  role VARCHAR(30),
  movieID INTEGER,
  actorID INTEGER
);"""
c.execute(create_table_statement)
conn.commit()
conn.close()