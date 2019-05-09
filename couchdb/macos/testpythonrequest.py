import requests

URL = "http://user:pass@localhost:5984/_cluster_setup"
my_proxies ={'http':None      }
r = requests.get(URL,allow_redirects=False)
contents = open('design.json', 'rb').read()
dURL = "http://user:pass@localhost:5984/dev-task/_design/task"
myrequest = requests.post(dURL,contents)
print("my content")
print(myrequest.content)
print("content")
print(r.content)
print("proxy content")
b = requests.get(URL,proxies=my_proxies,allow_redirects=False)
print(b.content)

