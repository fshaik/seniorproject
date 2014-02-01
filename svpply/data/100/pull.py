
import urllib2
import json
import MySQLdb as mdb
import random

cur = 0;
database = 'Svpply100Users';
tablename = 'user'

def addToDatabase(userId, productId, numwants):
  cur.execute("SELECT * FROM user WHERE id=" + str(userId))

  rows = cur.fetchall()

  
 # check if the user ! exists
			#add user row
  if len(rows) == 0:
    cur.execute("INSERT INTO " + tablename + " (id, numwants) " + "VALUES (" + str(userId)+", "+ str(numwants) + ")" )
    
			
		#check if ! pid exists
		#	add pid col

  cur.execute("SELECT * FROM information_schema.COLUMNS WHERE TABLE_SCHEMA = '" + database + 		"' AND COLUMN_NAME = 'p" + str(productId) + "'")

  rows = cur.fetchall()

  if len(rows) ==0:
    cur.execute("ALTER TABLE " + tablename +" ADD COLUMN p" + str(productId) + " INT DEFAULT 0")
  
  cur.execute("UPDATE " + tablename + " SET p" + str(productId) + "=1 WHERE id=" + str(userId))

def getProductsUserWants(userId):
  
  url = "https://api.svpply.com/v1/users/" + str(userId) + "/wants/products.json"
  
  try:
    response  = urllib2.urlopen(url)
  except :
    print "invalid Url: " + url 
    return
  
  responseObj = json.loads(response.read())

  if responseObj['meta']['status'] != 200:
    print "Http Error"
    return;


  responseProducts = responseObj['response']["products"]
  
  print len(responseProducts)

  for product in responseProducts:
  	if product['category'] == 'apparel':
  	  addToDatabase(userId, product['id'], len(responseProducts))

def chooseUser():
  return random.randint(1000,9000)

def main():
  con = mdb.connect('localhost', 'root', 'Rbak21rbak21', database)
  with con:
    global cur 
    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS user")
    cur.execute("CREATE TABLE user(id INT PRIMARY KEY, numwants INT)")

    for x in range(0, 99):
      userId = chooseUser()
      getProductsUserWants(userId)
 	  
    #cur.execute("INSERT INTO SvpplyUsers(userId) VALUES(" + str(userId) + ")")
