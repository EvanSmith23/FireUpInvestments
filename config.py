from flask import *
import MySQLdb
import os
import hashlib
from werkzeug import secure_filename
import glob

def connect_to_database():
    options = {
    'host': '0.0.0.0',
    'user': 'root',
    'passwd': 'newpass',
    'db': 'FireUpInvestments',
    'cursorclass' : MySQLdb.cursors.DictCursor
    }
    db = MySQLdb.connect(**options)
    db.autocommit(True)
    return db
