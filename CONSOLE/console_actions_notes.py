#!/usr/bin/python

'''

'''

import MySQLdb
import subprocess
import logging
logging.basicConfig(filename="D:\\ALLUSTORE\\alluCloud\\alluCloud.log",level=logging.DEBUG)

### MYSQL
LOCAL_ENV = ['localhost','root','alluCloudPassword','notedb']
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



def add_note(newNote = "NoValueHere"):
    #This is the console part
    if newNote == "NoValueHere":
        print "------------------"
        newNote = raw_input("New note :")
        query = "INSERT INTO notes (allNotes) VALUES('%s')" % (newNote)
        insert_database(query)
        selectQuery = "SELECT * FROM notedb.notes where allNotes = '%s'" % (newNote)
        if select_from_datebase(selectQuery)[0][1] == str(newNote):
            print "OK! Database was updated"
            logging.info('New note added to DB from Console: %s' %newNote)
        else:
            print "Something went wrong. The database query failed to find the new data!"
            logging.warning('Failed to add new note to DB from Console: %s' %newNote)
    else:
    #This is the part which takes input from the WebInterface
        query = "INSERT INTO notes (allNotes) VALUES('%s')" % (newNote)
        insert_database(query)
        selectQuery = "SELECT * FROM notedb.notes where allNotes = '%s'" % (newNote)
        if select_from_datebase(selectQuery)[0][1] == str(newNote):
            logging.info('New note added to DB from WebInterface: %s' %newNote)
        else:
            logging.warning('Failed to add new note to DB from WebInterface: %s' %newNote)

def select_from_datebase(selectQuery):
    db = MySQLdb.connect(db_server, db_user, db_password, default_table)
    cursor = db.cursor()
    cursor.execute(selectQuery)
    result = cursor.fetchall()
    return result
    db.close()

def list_notes():
    print "------------------"
    selectAllNotes = "SELECT * FROM notedb.notes"
    notesDict = select_from_datebase(selectAllNotes)
    for n in notesDict:
        print n[0]," : ",n[1]

def delete_note():
    print "------------------"
    selectAllNotes = "SELECT * FROM notedb.notes"
    notesDict = select_from_datebase(selectAllNotes)
    for n in notesDict:
        print n[0]," : ",n[1]
    deleteNote = raw_input("Which note ID to delete?:  ")
    query = "DELETE FROM notes WHERE noteID = '%s'" % (deleteNote)
    insert_database(query)
    selectQuery = "SELECT * FROM notedb.notes where noteID = '%s'" % (deleteNote)
    if select_from_datebase(selectQuery) == int(deleteNote):
        print "Something went wrong. The database still has that note!"
    else:
        print "OK! Note was removed"
    
    
