import qbittorrentapi
import mysql.connector
import mysqldatabase
import addtorrent
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


cnx.close()


def starttorrentadder():
    for torrent in qbt_client.torrents_info():
        print(f'{torrent.hash[-6:]}: {torrent.name} ({torrent.state})')
    getnodownlarr = mysqldatabase.getnodownl(cnx.cursor())
    for x in getnodownlarr:
        moviearr = mysqldatabase.getdata(cnx.cursor(),x[0])
        for x in moviearr:
            a = addtorrent.addmagnet(qbt_client,x.Hash)
            x.Path = addtorrent.getfoldername(qbt_client,x.Hash)
            mysqldatabase.setdata(cnx.cursor(),x)
            print(x.Hash) 

   