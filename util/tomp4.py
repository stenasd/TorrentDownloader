import moviepy.editor as moviepy
import os
from os import listdir
from os.path import isfile, join
import shutil
#delets all files thats less then 100mb
#make converttomp4 multithreaded
#to run at low traffic when adding new content
#torrent will be named after hash and put in a big move dir and all old is deleted
#check if publised

def converttomp4(file,newname):
    clip = moviepy.VideoFileClip(file)
    clip.write_videofile(newname+".mp4")
    shutil.move(newname+".mp4", './movies/'+newname+".mp4")


    
    

#torrentfolder will raname and move if mp4 and convert to mp4 then rename and move
def convertandmovetorrent(torrentfolder):
    onlyfiles = listdir(torrentfolder)
    for files1 in onlyfiles:
        files = os.path.join(torrentfolder, files1)
        print("py"in files)
        print(files)
        #comaprefile and if it contains pathname then
        if os.stat(files).st_size >100000000:
            if "mkv"in files:
                converttomp4(files,torrentfolder)
            if "avi"in files:
                #converttomp4 move and delete old files 
                print("movietoconvert")
                #converttomp4(files,"bigdick")
            if "mp4"in files:
                shutil.move(files, './movies/'+torrentfolder+".mp4")
        
 #(".",True)