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

pURL = "http://user:pass@localhost:5984/twitter"
db = requests.put(pURL,proxies = p).content
print(db)

by_hashtag = open('by_hashtag.json', 'rb').read()
hURL = "http://user:pass@localhost:5984/twitter/_design/by_hashtag"
r1 = requests.put(hURL,data=by_hashtag,proxies = p)
print(r1.content)

by_lga = open('by_lga.json', 'rb').read()
lURL = "http://user:pass@localhost:5984/twitter/_design/by_lga"
r2 = requests.put(lURL,data=by_lga,proxies = p)
print(r2.content)

by_word = open('by_word.json', 'rb').read()
dURL = "http://user:pass@localhost:5984/twitter/_design/by_word"
r3 = requests.put(dURL,data=by_word,proxies = p)
print(r3.content)








