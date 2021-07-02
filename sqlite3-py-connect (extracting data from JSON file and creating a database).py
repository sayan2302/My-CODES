import sqlite3
import json

conn=sqlite3.connect('C:/Users/SAYAN - NITRO 5/Desktop/sayan.sqlite')
cur=conn.cursor()

cur.executescript(
    '''
    drop table if exists user;
    drop table if exists course;
    drop table if exists member;

    create table user(
        id integer not null primary key  autoincrement unique ,
        name text unique);

    create table course(
        id integer not null primary key autoincrement unique ,
        title text unique);

    create table member(
        user_id integer,
        course_id integer,
        role text,
        primary key (user_id,course_id));
    ''')

temp=open('D:/STUDY STUFF/10. COURSERA/Using Databases with Python    [4th Course]/Material/roster/roster_data_sample.json').read()
data=json.loads(temp)

for i in data:
    name=i[0]
    title=i[1]
    f=lambda x: 'Teacher' if x==1 else 'Student'
    role=f(i[2])
    cur.execute('insert or ignore into user(name) values(?)',(name,))
    cur.execute('select id from user where name=?',(name,))
    user_id=cur.fetchone()[0]

    cur.execute('insert or ignore into course(title) values(?)',(title,))
    cur.execute('select id from course where title=?',(title,))
    course_id=cur.fetchone()[0]

    cur.execute('insert or replace into member(user_id,course_id,role) values(?,?,?)',(user_id,course_id,role))

conn.commit()
cur.close()

