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
    password="",
    database='pythonmovie')



qbt_client = qbittorrentapi.Client(host='localhost:8080', username='admin', password='adminadmin')

try:
    qbt_client.auth_log_in()
except qbittorrentapi.LoginFailed as e:
    print(e)


getnodownlarr = mysqldatabase.getnodownl(cnx.cursor())
for x in getnodownlarr:
    moviearr = mysqldatabase.getdata(cnx.cursor(),x[0])
    for x in moviearr:

        addtorrent.getfoldername(qbt_client,x.Hash)
        a = addtorrent.addmagnet(qbt_client,x.Hash)
        print(x.Hash) 
        
cnx.close()