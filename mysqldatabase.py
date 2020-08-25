
#get data from undownloaded 
def getdata(cursor,iden):
    movieobjects=[]
    query = ("SELECT path, name, hash,id FROM movies WHERE id = %s")
    val =(iden,)
    cursor.execute(query,val)
    for (path, name, heshid,Id) in cursor:
        p1=movies(Id,name,path,heshid)
        movieobjects.append(p1)
    return movieobjects
#set everything except id
#objtosetdatafrom
def setdata(cursor,movieobj):
    query = ("UPDATE movies SET path = %s,name = %s,hash = %s, WHERE id = %s")
    val = (movieobj.Path, movieobj.Name, movieobj.Hash ,movieobj.Id)
    cursor.execute(sql, val)
    emp_no = cursor.lastrowid
    cnx.commit()
def getnodownl(cursor):
    nodownloadarr=[]
    query = ("SELECT id FROM nodownload")
    cursor.execute(query)
    for Id in cursor:
        nodownloadarr.append(Id)
    return nodownloadarr
def gettoprepare(cursor):
    nodownloadarr=[]
    query = ("SELECT id FROM nodownload")
    
    cursor.execute(query)
    for Id in cursor:
        nodownloadarr.append(Id)
       
    return nodownloadarr

class movies:
  def __init__(self,Id, Name, Path,Hash,):
    self.Name = Name
    self.Id = Id
    self.Path = Path
    self.Hash=Hash
  







            



