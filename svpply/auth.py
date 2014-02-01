import urllib2
import json

def getUsersWhoWantProduct():
  response  = urllib2.urlopen("https://api.svpply.com/v1/products/3678811/users.json")
  responseObj = json.loads(response.read())
  
  if responseObj['meta']['status'] != 200:
    return;

  responseData = responseObj['response']
  numUsers = responseData['total_users']
  
  for i in range(0, numUsers):
    print responseData["users"][i]["id"]

  return


def getProductsUserWants():
  
  response  = urllib2.urlopen("https://api.svpply.com/v1/users/1209324/wants/products.json")
  responseObj = json.loads(response.read())

  if responseObj['meta']['status'] != 200:
    print "Http Error"
    return;

  responseData = responseObj['response']

