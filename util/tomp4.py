import moviepy.editor as moviepy
import os
from os import listdir
from os.path import isfile, join
import shutil
raidpath = "/mnt/md0/"

def converttomp4(file,newname):
    clip = moviepy.VideoFileClip(file)
    clip.write_videofile(newname+".mp4")
    shutil.copy(newname+".mp4", raidpath+newname+".mp4")
    os.remove(newname+".mp4")
    #shutil.move(newname+".mp4", '/mnt/md0/'+newname+".mp4")

def convertandmovetorrent(files2,name):
    name = str(name)
    for files in files2:
        print("files")
        print(files.name)
        files = files.name
        files = "./movies/" + files
        #comaprefile and if it contains pathname then
        if os.stat(files).st_size >1:
            if "mkv"in files:
                converttomp4(files,name)
            if "avi"in files:
                converttomp4(files,name)
                print("movietoconvert")
                #converttomp4(files,"bigdick")
            if "mp4"in files:
                shutil.copy(files, raidpath+name+".mp4")
                os.remove(files)
#newname = "21"
#shutil.copy(newname+".mp4", raidpath+newname+".mp4")
#converttomp4("/home/stenasd/Documents/gitreps/TorrentDownloader/movies/testfolder/test.mkv","a1")

