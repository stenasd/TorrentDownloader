import qbittorrentapi
import mysql.connector
import mysqldatabase
import addtorrent
import tomp4
#todo creat movie obj class and test set data
torrentpath = "pathtotorrent"
readymoviepath="pathtoreadymovie"
cnx = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database='movies')

qbt_client = qbittorrentapi.Client(host='localhost:8080', username='admin', password='adminadmin')

try:
    qbt_client.auth_log_in()
except qbittorrentapi.LoginFailed as e:
    print(e)

for torrent in qbt_client.torrents_info():
    print(f'{torrent.availability}: {torrent.name} ')
    if torrent.availability == -1:  
        print("asd")
        movobj = mysqldatabase.getdatafrompath(cnx.cursor(),torrent.name)
        tomp4.convertandmovetorrent(torrent.name)
        mysqldatabase.deltodownload(cnx.cursor(),movobj[0].Id)
        mysqldatabase.inserttostream(cnx.cursor(),movobj[0].Id)
        qbt_client.torrents_delete(True,torrent.hash)
      #del from todownload
      #add ready to stream
      #foldername match movieobj id
    #if torrent ==-1 send torrent name to converttorrent
cnx.commit()
cnx.close()


#magnet_uri
#({torrent.hash})