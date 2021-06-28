#-------------------------import sqlite3 module------------------------
import sqlite3


#--------------------------creating & connecting to DB----------------- 
conn=sqlite3.connect('C:/Users/SAYAN - NITRO 5/Desktop/sayandb.sqlite')
cur=conn.cursor()


#-------------------------------query1---------------------------------
cur.execute('drop table if exists counts')


#-------------------------------query2---------------------------------
cur.execute('create table counts(email varchar(30),count int(3))')


#------------------------------file-name-------------------------------
fname=input('Enter file name : ')
if len(fname)<1: fname='mbox-short.txt'

    
#------------------------------file-handle-----------------------------
fhand=open(fname)
for line in fhand:
    if not line.startswith('From: '):
        continue
    words=line.split()
    email=words[1]
    
    
#-----------------------------email-count------------------------------
    cur.execute('select count from counts where email=?',(email,))
    row=cur.fetchone()

    
#-----------------------------frequency check--------------------------
    if row is None:
        cur.execute('insert into counts values (?,1)',(email,))
    else:
        cur.execute('update counts set count=count+1 where email=?',(email,))

        
#-----------------------------saving database--------------------------
conn.commit()


#------------------------showing result in terminal--------------------
query='select * from counts order by email'
for i in cur.execute(query):
    print(i[0],i[1])

    
#---------------------------closing cursor-----------------------------
cur.close()
