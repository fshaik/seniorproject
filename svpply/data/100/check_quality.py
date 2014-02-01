import MySQLdb as mdb

cur = 0;
database = 'Svpply100Users';
tablename = 'user'

productids = []
userids = []

def findSize():
  global userids
  global productids

  cur.execute("SELECT id FROM " + tablename)
  userids = cur.fetchall()

  cur.execute("SELECT column_name FROM information_schema.columns WHERE table_name = '" + tablename + "' and table_schema ='" + database +"'")
  productids = cur.fetchall()

  return len(productids) * len(userids)



def connectToDatabase():
  con = mdb.connect('localhost', 'root', 'Rbak21rbak21', database, charset='utf8')
  with con:
    global cur 
    cur = con.cursor()


def main():
  connectToDatabase()
  print findSize()

if __name__ == "__main__":
  main()