import requests


nodes = [ ("172.20.0.2","5984"), ("172.20.0.3","15984") ,("172.20.0.4","25984")]
masternode = nodes[0]


for address in nodes:
    URL = "http://user:pass@localhost:%s/_cluster_setup" % (address[1])
    print(URL)
    r = requests.post(URL,json={"action":"enable_cluster","bind_address":"0.0.0.0"
    ,"username":"user","password":"pass","node_count":"3"})

    print(r.json())

for address in nodes:
    URL = "http://user:pass@localhost:%s/_cluster_setup" % (masternode[1])
    print(URL)
    if(address != masternode):
        r = requests.post(URL,json={"action":"enable_cluster","bind_address":"0.0.0.0"
         ,"username":"user","password":"pass","port":"5984","node_count":f"nodes.__len__()",
         "remote_node": f"address[0]", "remote_current_user": "user", "remote_current_password": "pass"})
        print(r.json())
        r = requests.post(URL, json={
            "action": "add_node",
            "host": address[0],
            "port": "5984",
            "username":"user",
            "password":"pass"


        })

        print(r.json())

URL = "http://user:pass@localhost:%s/_cluster_setup" % (masternode[1])

r = requests.post(URL, json={
            "action": "finish_cluster",
        })

print(r.json())

print(requests.get(URL))

for address in nodes:
    URL = f"http://user:pass@localhost:address[1]/_membership"
    print(requests.get(URL))




