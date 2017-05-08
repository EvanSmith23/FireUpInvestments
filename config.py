from flask import *
import MySQLdb
import os
import hashlib
from werkzeug import secure_filename
import glob

def connect_to_database():
    
    # creating arguments for connect function
    options = 
    {
    'host': '0.0.0.0',
    'user': 'root',
    'passwd': 'new',
    'db': 'FireUp',
    'cursorclass' : MySQLdb.cursors.DictCursor
    }
    
    #connecting to database with parameters passed in
    db = MySQLdb.connect(**options)
    db.autocommit(True)
    
    #returns a connection object from MYSQLDB
    return db
