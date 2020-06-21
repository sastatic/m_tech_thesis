from pymongo import MongoClient

def dbconfig(
    DB_NAME='thesis_sarwar',
    DB_HOST='mongodb://admin:admin123@ds137651.mlab.com:37651/thesis_sarwar',
    DB_PORT=37651,
    DB_USER='admin',
    DB_PASS='admin123'
  ):
  try:
    connection = MongoClient(DB_HOST, DB_PORT)
    db = connection[DB_NAME]
    db.authenticate(DB_USER, DB_PASS)
    return(db, True)
  except Exception as exc:
    print('Error while connecting', exc)
    return(None, False)
