import moviepy.editor as moviepy
import os
from os import listdir
from os.path import isfile, join
import shutil


def converttomp4(file,newname):
    clip = moviepy.VideoFileClip(file)
    clip.write_videofile(newname+".mp4")
    shutil.move(newname+".mp4", '/mnt/md0/'+newname+".mp4")

def convertandmovetorrent(torrentfolder):
    torrentfolder = "./movies/"+torrentfolder
    onlyfiles = listdir(torrentfolder)
    for files1 in onlyfiles:
        files = os.path.join(torrentfolder, files1)
        print("py"in files)
        print(files)
        #comaprefile and if it contains pathname then
        if os.stat(files).st_size >50000000:
            if "mkv"in files:
                converttomp4(files,torrentfolder)
            if "avi"in files:
                converttomp4(files,torrentfolder)
                print("movietoconvert")
                #converttomp4(files,"bigdick")
            if "mp4"in files:
                shutil.move(files, './movies/'+torrentfolder+".mp4")
def convertandmovetorrent1(qbt_client,magnet):
    torrentfolder = "./movies/"+torrentfolder
    onlyfiles = listdir(torrentfolder)
    for files1 in onlyfiles:
        files = os.path.join(torrentfolder, files1)
        print("py"in files)
        print(files)
        #comaprefile and if it contains pathname then
        if os.stat(files).st_size >50000000:
            if "mkv"in files:
                converttomp4(files,torrentfolder)
            if "avi"in files:
                converttomp4(files,torrentfolder)
                print("movietoconvert")
                #converttomp4(files,"bigdick")
            if "mp4"in files:
                shutil.move(files, './movies/'+torrentfolder+".mp4")
        
 #(".",True)