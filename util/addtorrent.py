
import time
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
    #make separate that updates all paths if possilbe and ignore converting if no path or just keep running update script every 5 min or somethin       
    files = " "
    try:
        files = qbt_client.torrents_files(hash=(gethash(qbt_client,magnet)))
        for file in files:
            print(file.name)
        return files[0].name.split("/")[0]
    except:
        pass
def gethash(qbt_client,magnet):
    
    torrent_list = qbt_client.torrents_info()
    for torrent in torrent_list:
        
        uri = torrent.magnet_uri[0:60]
        mag = magnet[0:60]
        uri = uri.lower()
        mag = mag.lower()
        if uri==mag:
            files = qbt_client.torrents_files(hash=(torrent.hash))
            print("hash"+torrent.hash)
            return torrent.hash




    