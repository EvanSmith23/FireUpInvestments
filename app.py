from flask import *
import MySQLdb
import os
import hashlib
from werkzeug import secure_filename
import glob
import json
from config import connect_to_database

def get_house_data():

	db = connect_to_database()

	print "here"

	albumquery = "SELECT * FROM houses"
	cur = db.cursor()
	cur.execute(albumquery)
	albumresult = cur.fetchall()[0]

	print jsonify(address=albumresult['address'],city=albumresult['city'],state=albumresult['state'],zipcode=albumresult['zipcode'],description=albumresult['desription'],house_id=albumresult['house_id'])

	return
