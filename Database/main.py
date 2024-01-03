import sqlite3

def printTable(c):
  result = c.fetchall()
  for r in result:
    r = str(r)
    r = r.replace("(", "")
    r = r.replace(")", "")
    r = r.replace(",", "")
    print(r)
def getUsers():
  conn = sqlite3.connect("database.db")
  c = conn.cursor()
  c.execute("SELECT * FROM users")
  printTable(c)
  conn.commit()
  conn.close()
def getMovie():
  conn = sqlite3.connect("database.db")
  c = conn.cursor()
  c.execute("SELECT * FROM movies")
  printTable(c)
  conn.commit()
  conn.close()
def getActors():
  conn = sqlite3.connect("database.db")
  c = conn.cursor()
  c.execute("SELECT * FROM actor")
  printTable(c)
  conn.commit()
  conn.close()
def trimResult(result:str):
  result = result.replace("(", "")
  result = result.replace(")", "")
  result = result.replace("[", "")
  result = result.replace("]", "")
  result = result.replace(",", "")
  return result
def findMovieID(movieName):
  conn= sqlite3.connect("database.db")
  c= conn.cursor()
  fetch_statement= """SELECT movieID FROM movies WHERE movieName= ? """
  c.execute(fetch_statement,(movieName,))
  result=str(c.fetchall())
  if result=="[]":
    return False
  result=int(trimResult(result))
  conn.commit()
  conn.close()
  return result
def findUserID(username):
  conn = sqlite3.connect("database.db")
  c = conn.cursor()
  fetch_statement = """SELECT userID FROM users WHERE username= ? """
  c.execute(fetch_statement, (username,))
  result = str(c.fetchall())
  if result == "[]":
    return False
  result = int(trimResult(result))
  conn.commit()
  conn.close()
  return result
def makeReview(username,movieName,score):
  if findMovieID(movieName)==False:
    print("movie not found")
    return
  elif findUserID(username)==False:
    print("username not found")
    return
  userID=findUserID(username)
  movieID=findMovieID(movieName)
  conn = sqlite3.connect("database.db")
  c = conn.cursor()
  insert_statement = """INSERT INTO review (userID,movieID,score) VALUES (?,?,?);"""
  c.execute(insert_statement, (userID, movieID, score))
  conn.commit()
  conn.close()
def getAverageRating(movieName):
  if findMovieID(movieName)==False:
    print("movie not found")
    return
  movieID=findMovieID(movieName)
  conn= sqlite3.connect("database.db")
  c= conn.cursor()
  fetch_statement = """SELECT AVG(score) FROM review WHERE movieID=?;"""
  c.execute(fetch_statement, (movieID,))
  result=str(c.fetchall())
  if result=="[(None,)]":
    print("No reviews yet")
    return
  print(trimResult(result))
  conn.commit()
  conn.close()
  return
def getAllRatings(movieName):
  conn= sqlite3.connect("database.db")
  c= conn.cursor()
  if findMovieID(movieName)==False:
    print("No movie found")
    return
  movieID=findMovieID(movieName)
  fetch_statement= """SELECT score FROM review WHERE movieID=?"""
  c.execute(fetch_statement,(movieID,))
  printTable(c)
  conn.commit()
  conn.close()

exit=True
while exit:
  option= input("What would you want to do"+"\n"
                    +"1: View all users"+"\n"
                    +"2: View all movies"+"\n"
                    +"3: View all actor"+"\n"
                    +"4: Make a review"+"\n"
                    +"5: Find average rating"+"\n"
                    +"6: View all reviews"+"\n")
  ## check that input is a number
  try:
    option=int(option)
  except ValueError:
    print("Input is not an integer")
  if option==1:
    getUsers()
  elif option==2:
    getMovie()
  elif option==3:
    getActors()
  elif option==4:
    user = input("Enter your username")
    movie = input("Enter the movie name")
    score = float(input("Enter your rating"))
    makeReview(user,movie,score)
  elif option==5:
    movie= input("What movie would you want a review rating for")
    getAverageRating(movie)
  elif option==6:
    movie = input("What movie would you want to see reviews for")
    getAllRatings(movie)
  else:
    print("I assume that you want to stop, thank you for using this service")
    break
  exit=bool(input("Press any key then press enter to continue"))


