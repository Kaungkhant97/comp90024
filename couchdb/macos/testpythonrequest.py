import requests

URL = "http://user:pass@localhost:5984/_cluster_setup"
my_proxies ={'http':'http://wwwproxy.unimelb.edu.au:8000',
'https':'https://wwwproxy.unimelb.edu.au:8000'}
r = requests.get(URL)
print("content")
print(r.content)
print("proxy content")
b = requests.get(URL,proxies=my_proxies)
print(b.content)

