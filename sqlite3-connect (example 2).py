import sqlite3
conn=sqlite3.connect('C:/Users/SAYAN - NITRO 5/Desktop/sayandb.sqlite')
cur=conn.cursor()
cur.execute('drop table if exists cola')
cur.execute('create table cola(word varchar(10),count int(5))')

fh=open('romeo.txt')

for line in fh:
    line=line.strip()
    words=line.split()
    for i in words:
        cur.execute('select count from cola where word=?',(i,))
        row=cur.fetchone()

        if row is None:
            cur.execute('insert into cola values(?,1)',(i,))
        else:
            cur.execute('update cola set count=count+1 where word=?',(i,))
conn.commit()
query='select * from cola'

for i in cur.execute(query):
    if str(i[0]).lower() == 'romeo':
        print(i[0],i[1])
cur.close()
