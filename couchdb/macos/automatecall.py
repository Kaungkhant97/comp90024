import requests

URL = "http://user:pass@localhost:5984/_cluster_setup"

r = requests.post(URL,json={"action":"enable_cluster","bind_address":"0.0.0.0"
    ,"username":"user","password":"pass","node_count":"3"})

m = r.json()

print(m)