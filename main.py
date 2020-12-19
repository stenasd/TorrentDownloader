import sys
sys.path.insert(0, 'util')
import qbittorrentapi
import mysql.connector
import mysqldatabase
import addtorrent
import tomp4
import schedule
import time
cnx = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="stenroot",
    database='movies')
#TODO remove from nodownload table
qbt_client = qbittorrentapi.Client(host='localhost:8080', username='admin', password='stenadmin')

try:
    qbt_client.auth_log_in()
except qbittorrentapi.LoginFailed as e:
    print(e)


#todo creat movie obj class and test set data
def startconverter():  
    print("startconverter started")
    for torrent in qbt_client.torrents_info():
        print(f'{torrent.availability}: {torrent.name} ')
        if torrent.availability == -1:  
            print("asd")
            movobj = mysqldatabase.getdatafrompath(cnx.cursor(),torrent.name)
            files = addtorrent.getfoldername1(qbt_client,movobj[0].Hash)
            tomp4.convertandmovetorrent(files,movobj[0].Id)
            mysqldatabase.deltodownload(cnx.cursor(),movobj[0].Id)
            mysqldatabase.inserttostream(cnx.cursor(),movobj[0].Id)
            qbt_client.torrents_delete(True,torrent.hash)
        #del from todownload
        #add ready to stream
        #foldername match movieobj id
        #if torrent ==-1 send torrent name to converttorrent
def starttorrentadder():
    print("starttorrentadder started")
    getnodownlarr = mysqldatabase.getnodownl(cnx.cursor())
    for x in getnodownlarr:
        moviearr = mysqldatabase.getdata(cnx.cursor(),x[0])
        for x in moviearr:
            a = addtorrent.addmagnet(qbt_client,x.Hash)
            x.Path = addtorrent.getname(qbt_client,x.Hash)
            mysqldatabase.setdata(cnx.cursor(),x)
            cnx.commit()
            print(x.Hash)
def starttorrentadder1():
    print("starttorrentadder started")
    getnodownlarr = mysqldatabase.getnodownl(cnx.cursor())
    for x in getnodownlarr:
        moviearr = mysqldatabase.getdata(cnx.cursor(),x[0])
        for x in moviearr:
            #a = addtorrent.addmagnet(qbt_client,x.Hash)
            x.Path = addtorrent.getfoldername(qbt_client,x.Hash)
            print(x.Path)
            #mysqldatabase.setdata(cnx.cursor(),x)
            #cnx.commit()
startconverter()         
#starttorrentadder()
#schedule.every(5).minutes.do(starttorrentadder)
#schedule.every().hour.do(startconverter)
while True:
    schedule.run_pending()
    time.sleep(1)
cnx.commit()
cnx.close()


#magnet_uri
#({torrent.hash})