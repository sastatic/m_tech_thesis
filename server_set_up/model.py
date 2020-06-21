from dbconfig import dbconfig

def main(data):
    db, dbconnected = dbconfig()
    if not dbconnected:
        print("not connected to database, no caching of result")
        return
    db.reports.insert_one(data).inserted_id
    print ("Report successfully updated.")
    return True
