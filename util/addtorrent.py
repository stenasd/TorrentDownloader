
def addmagnet(apiclient,magnet):
    apiclient.torrents_add(urls=magnet,is_root_folder=True)
    #print("torrent added")
def getfoldername1(apiclient,magnet):
    for torrent in apiclient.torrents_info():
        uri = torrent.magnet_uri[0:60]
        mag = magnet[0:60]
        uri = uri.lower()
        mag = mag.lower()
        print("1 "+uri)
        print("2 "+mag)
        if uri==mag:
            print("match")
            return torrent.name
            #test
            #https://stackoverflow.com/questions/42541748/rename-and-move-file-with-python
def getfoldername(qbt_client,magnet):
        properties = qbt_client.torrents_properties(hash=(magnet))
        files = qbt_client.torrents_files(hash=(magnet))
        return files[0].name.split("/")[0]




    