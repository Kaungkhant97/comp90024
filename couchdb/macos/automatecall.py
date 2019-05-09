import requests



nodes = [ ("172.20.0.2","5984"), ("172.20.0.3","15984") ,("172.20.0.4","25984")]
masternode = nodes[0]
p ={'http': None
            }

for address in nodes:
    URL = "http://user:pass@localhost:%s/_cluster_setup" % (address[1])
   # print(URL)

    r = requests.post(URL,json={"action":"enable_cluster","bind_address":"0.0.0.0"
    ,"username":"user","password":"pass","node_count":"3"},proxies = p)

    print(r.content)

for address in nodes:
    URL = "http://user:pass@localhost:%s/_cluster_setup" % (masternode[1])
    print(URL)
    if(address != masternode):
        r = requests.post(URL,json={"action":"enable_cluster","bind_address":"0.0.0.0"
         ,"username":"user","password":"pass","port":"5984","node_count":f"nodes.__len__()",
         "remote_node": f"address[0]", "remote_current_user": "user", "remote_current_password": "pass"},proxies = p)
        print(r.content)
        r = requests.post(URL, json={
            "action": "add_node",
            "host": address[0],
            "port": "5984",
            "username":"user",
            "password":"pass"


        },proxies = p)

        print(r.json())

address = "http://user:pass@localhost:5984/_cluster_setup"
print(address)
r = requests.post(address, json={
            "action": "finish_cluster",
        },proxies = p)

print(r.content)
r = requests.get(address,proxies = p)
print(r.content)

for address in nodes:

    murl = "http://user:pass@localhost:%s/_membership" %address[1]
    print(murl)
    r =requests.get(murl,proxies = p)
    print(r.content)


contents = open('design.json', 'rb').read()
dURL = "http://user:pass@localhost:5984/dev-task/_design/task"
myrequest = requests.post(dURL,contents)
print(myrequest.content)

URL = "http://user:pass@localhost:5984/twitter"
db = requests.put(URL).content
print(db)



