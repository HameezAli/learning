from sqlalchemy import create_engine, text, MetaData, Table, Column, Integer, String, insert, ForeignKey, Float, func
from sqlalchemy.orm import Session # Object Relational Mapper

# Core connection
engine = create_engine("mssql+pyodbc://@DESKTOP-M8HIIN2\\SQLEXPRESS02/sqlalc?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes",echo=True)
conn=engine.connect().execution_options(isolation_level="AUTOCOMMIT")
print('Connection success!')

# operations using vanilla sql
# conn.execute(text("create table students(sname varchar(50),regno int);"))
#conn.commit()

# Session connection
#session = Session(engine)
#session.execute(text("insert into students (sname,regno) values ('Hameez',14);"))
#session.commit()

# Create table from python sqlalchemy
meta=MetaData()
friends=Table( # python object name
     "friends",meta, # table name
     Column('fid',Integer, primary_key=True),
     Column('age',Integer), # column name and datatype which were imported above
     Column('name',String),
     Column('dept',String)
 )

#Creating tables with relationships
things=Table(
    "things", meta,
    Column('tid',Integer,primary_key=True),
    Column('tname',String),
    Column('price',Float),
    Column('Owner',Integer,ForeignKey('friends.fid'))
)
# meta.create_all(engine)

#  # inserting using sqlalchemy core functions
# insert_st = friends.insert().values(name='Giri',age=20,dept='DS')
# insert_st1 = insert(friends).values(name='Rahul',age=21,dept='DS')
# conn.execute(insert_st)
# conn.commit() # Changes need to be commited, else will not be saved to the database

# # Update using sqlalchemy core
# update_st = friends.update().where(friends.c.name=='Giri').values(name='Paraman')
# result = conn.execute(update_st)
# conn.commit()

# # Delete using sqlalchemy core
# delete_st = friends.delete().where(friends.c.age==20)
# result = conn.execute(delete_st)
# conn.commit()

# selecting using sqlalchemy core
select_st = friends.select()#.where(friends.c.age == 19)
result = conn.execute(select_st)
for r in result.fetchall():
    print(r)

# insert multiple items
insert_friends = friends.insert().values([
    {'fid':1,'name':'Giri','age':20,'dept':'DS'},
    {'fid':2,'name':'Hari','age':21,'dept':'CS'},
    {'fid':3,'name':'Saran','age':22,'dept':'IT'},
    {'fid':4,'name':'Rahul','age':23,'dept':'AIML'},
    {'fid':5,'name':'Hameez','age':24,'dept':'CSBS'}
])

insert_things = things.insert().values([
    {'tid':1,'tname':'Laptop','price':40000,'Owner':1},
    {'tid':2,'tname':'Laptop','price':45000,'Owner':2},
    {'tid':3,'tname':'Iphone','price':84000,'Owner':3},
    {'tid':4,'tname':'Bike','price':72000,'Owner':4},
    {'tid':5,'tname':'Car','price':500000,'Owner':5},
    {'tid':6,'tname':'Car','price':750000,'Owner':2}
])

# conn.execute(insert_friends)
# conn.execute(insert_things)
# print('Insert Successful!')

# # Join statement
# join_st = friends.join(things,friends.c.fid==things.c.Owner)
# selst = friends.select().with_only_columns(friends.c.name,things.c.tname).select_from(join_st)
# res = conn.execute(selst)
# for r in res.fetchall():
#     print(r)

# group by statement
# group_st = things.select().with_only_columns(things.c.Owner,func.sum(things.c.price)).group_by(things.c.Owner).having(func.sum(things.c.price)<=100000)
# res = conn.execute(group_st)
# for r in res.fetchall():
#     print(r)