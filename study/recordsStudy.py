import json # https://docs.python.org/3/library/json.html
import requests # https://github.com/kennethreitz/requests
import records # https://github.com/kennethreitz/records


'''数据库连接 
"""PostgreSQL"""
# default
db = records.Database('postgresql://scott:tiger@localhost/mydatabase')
# psycopg2
db = records.Database('postgresql+psycopg2://scott:tiger@localhost/mydatabase')
# pg8000
db = records.Database('postgresql+pg8000://scott:tiger@localhost/mydatabase')


"""MySQL"""
# default
db = records.Database('mysql://scott:tiger@localhost/foo')
# mysqlclient (a maintained fork of MySQL-Python)
db = records.Database('mysql+mysqldb://scott:tiger@localhost/foo')
# PyMySQL
db = records.Database('mysql+pymysql://scott:tiger@localhost/foo')

"""Oracle"""
db = records.Database('oracle://scott:tiger@127.0.0.1:1521/sidname')
db = records.Database('oracle+cx_oracle://scott:tiger@tnsname')

"""Microsoft SQL Server"""
# pyodbc
db = records.Database('mssql+pyodbc://scott:tiger@mydsn')
# pymssql
db = records.Database('mssql+pymssql://scott:tiger@hostname:port/dbname')

"""SQLite"""
# for a relative file path
db = records.Database('sqlite:///foo.db')
# for a absolute file path 
# UNIX/MAC
db = records.Database('sqlite:////absolute/path/to/foo.db')
# Windows
db = records.Database('sqlite:///C:\\path\\to\\foo.db')
# Windows using raw string
db = records.Database(r'sqlite:///C:\path\to\foo.db')
# for a memory database
db = records.Database('sqlite://')'''

# randomuser.me generates random 'user' data (name, email, addr, phone number, etc)
r = requests.get('http://api.randomuser.me/0.6/?nat=us&results=10')
j = r.json()['results']
# print(j)
db = records.Database('sqlite:///users.db')
conn = db.get_connection()
conn.query('DROP TABLE IF EXISTS persons')
conn.query('CREATE TABLE persons (key int PRIMARY KEY, fname text, lname text, email text)')

for rec in j:
    user = rec['user']
    name = user['name']
    key = user['registered']
    fname = name['first']
    lname = name['last']
    email = user['email']
    db.query('INSERT INTO persons (key, fname, lname, email) VALUES(:key, :fname, :lname, :email)',
            key=key, fname=fname, lname=lname, email=email)

# print (rows.dataset)
rows = conn.query('SELECT * FROM persons')
print(rows.export('csv'))
with open('json.csv','w',newline='',encoding='utf-8') as  f:
    f.write(rows.export('csv'))
