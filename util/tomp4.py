import moviepy.editor as moviepy
import os
from os import listdir
from os.path import isfile, join
import shutil


def converttomp4(file,newname):
    clip = moviepy.VideoFileClip(file)
    clip.write_videofile(newname+".mp4")
    shutil.move(newname+".mp4", './movies/'+newname+".mp4")
    #shutil.move(newname+".mp4", '/mnt/md0/'+newname+".mp4")

def convertandmovetorrent(files2,name):
    name = str(name)
    for files in files2:
        print("files")
        print(files.name)
        files = files.name
        files = "./movies/" + files
        #comaprefile and if it contains pathname then
        if os.stat(files).st_size >50000000:
            if "mkv"in files:
                converttomp4(files,name)
            if "avi"in files:
                converttomp4(files,name)
                print("movietoconvert")
                #converttomp4(files,"bigdick")
            if "mp4"in files:
                shutil.move(files, './movies/'+name+".mp4")