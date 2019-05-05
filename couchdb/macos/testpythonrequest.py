import requests

URL = "http://user:pass@localhost:5984/_cluster_setup"
my_proxies ={'http_proxy':'http://wwwproxy.unimelb.edu.au:8000',
'https_proxy':'https://wwwproxy.unimelb.edu.au:8000'}
r = requests.get(URL)
print(r.content)