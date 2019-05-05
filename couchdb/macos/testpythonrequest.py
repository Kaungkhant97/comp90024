import requests

URL = "http://user:pass@localhost:5984/_cluster_setup"
my_proxies ={'http':'http://www.proxy.unimelb.edu.au:8000',
'https':'https://www.proxy.unimelb.edu.au:8000'}
r = requests.get(URL)
print(r.content)
b = requests.get(URL,proxies=my_proxies)
print(b.content)

