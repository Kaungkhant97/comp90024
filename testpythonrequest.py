import requests

URL = "http://user:pass@localhost:5984/_cluster_setup"
my_proxies ={'http':'http://wwwproxy.unimelb.edu.au:8000',
'https':'https://wwwproxy.unimelb.edu.au:8000',
'no_proxy': 'localhost,http://user:pass@localhost'             }
r = requests.get(URL,allow_redirects=False)
print("content")
print(r.content)
print("proxy content")
b = requests.get(URL,proxies=my_proxies,allow_redirects=False)
print(b.content)

