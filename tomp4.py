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

#torrentfolder will raname and move if mp4 and convert to mp4 then rename and move
def convertandmovetorrent(torrentfolder,movieobj):
    onlyfiles = [f for f in listdir(torrentfolder) if isfile(join(".", f)) ]
    for files in onlyfiles:
        print(os.stat(files).st_size)
        print("py"in files)
        print(files)
        #moveobj.toprepare move and rename based on 
        if os.stat(files).st_size >100000000:
            if "avi"in files:
                #converttomp4 move and delete old files 
                print("movietoconvert")
                #converttomp4(files,"bigdick")
            if "mp4"in files:
                shutil.move('bigdick.mp4', 'mp4folder')
convertandmovetorrent(".",True)