#!/usr/bin/python

import MySQLdb
import subprocess

### MYSQL
LOCAL_ENV = ['localhost','root','neerg42','filmdb']
ENVIRONMENT = LOCAL_ENV
db_server = ENVIRONMENT[0]
db_user = ENVIRONMENT[1]
db_password = ENVIRONMENT[2]
default_table = ENVIRONMENT[3]

def insert_database(query):
    db = MySQLdb.connect(db_server, db_user, db_password, default_table)
    cursor = db.cursor()
    try:
        # Execute the SQL command
        cursor.execute(query)
        # Commit your changes in the database
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()

def add_film():
    filmTitleValue = raw_input("Name of Film:")
    filmCommentValue = raw_input("Comment:")
    query = "INSERT INTO titles (title,alreadySeen,yearSeen,monthSeen,comment) VALUES('%s', %s, %s, %s, '%s')" % (filmTitleValue,0,0,0,filmCommentValue)
    insert_database(query)
    selectTestQuery = "SELECT * FROM filmdb.titles where title = '%s' AND comment = '%s'" % (filmTitleValue,filmCommentValue)
    print select_from_datebase_as_test(selectTestQuery)[0][1]
    if select_from_datebase_as_test(selectTestQuery)[0][1] == str(filmTitleValue):
        if select_from_datebase_as_test(selectTestQuery)[0][2] == 0:
            print "OK! Database was updated"
        else:
            print "Something went wrong. The database query failed to find the new unseen film!"
    else:
        print "Something went wrong. The database query failed to find the new data!"

def select_from_datebase_as_test(selectTestQuery):
    db = MySQLdb.connect(db_server, db_user, db_password, default_table)
    cursor = db.cursor()
    cursor.execute(selectTestQuery)
    result = cursor.fetchall()
    return result
    db.close()
