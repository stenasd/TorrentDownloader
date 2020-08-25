
#returns name if torrents downloaded
def addmagnet(apiclient,magnet):
    apiclient.torrents_add(urls=magnet, save_path='..../',is_root_folder=True)
    #print("torrent added")
def getfoldername(apiclient,magnet):
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
            #https://stackoverflow.com/questions/42541748/rename-and-move-file-with-python
def getcompletedtorrents(apiclient):
    return True
    #return list of completed torrents
def removeFromToDownload(apiclient):

    #removes and add to toprepare
            
    