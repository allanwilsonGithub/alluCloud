#!/usr/bin/python

'''
Connections between cloud parts (FTP, MYSql, HTTP) for EVENT module
'''

import urllib2
import ftplib
from ftplib import FTP
import MySQLdb
import datetime
import smtplib
from email.MIMEText import MIMEText

#####HTTP
def get_index_html_from_allu_cloud_EVENT_by_HTTP():
    u = urllib2.urlopen('http://www.kolumbus.fi/allan.wilson/alluCloud/EVENT/indexTemplate.html')
    localFile = open('index.html', 'w')
    localFile.write(u.read())
    localFile.close()


###EMAIL
def send_mail(text):
   msg = MIMEText(text)
   msg['Subject'] = 'AlluCloud Event'
   msg['From'] = "AlluCloud"
   msg['Reply-to'] = "AlluCloud"
   msg['To'] = "allan@allanwilson.net"
   s = smtplib.SMTP()
   s.connect("smtp.dnainternet.net")
   s.sendmail("allan@allanwilson.net","allan@allanwilson.net", msg.as_string())
   s.close()

### MYSQL
LOCAL_ENV = ['localhost','root','neerg42','eventdb']
ENVIRONMENT = LOCAL_ENV
db_server = ENVIRONMENT[0]
db_user = ENVIRONMENT[1]
db_password = ENVIRONMENT[2]
default_table = ENVIRONMENT[3]

def get_version():
    db = MySQLdb.connect(db_server, db_user, db_password, default_table)
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")
    version = cursor.fetchone()
    db.close()
    return version
    
def query_database(query):
    db = MySQLdb.connect(db_server, db_user, db_password, default_table)
    cursor = db.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result
    db.close()

def count_all_events():
    query = query_database("SELECT count(eventName) FROM eventdb.events;")
    return query

def list_events(months):
    query = query_database("SELECT events.date, events.eventName, events.comment, eventtypes.typeName FROM events, eventtypes WHERE events.date between CURDATE() AND DATE_ADD(CURDATE(),INTERVAL %s MONTH) AND eventtypes.eventTypeID = events.eventType ORDER BY events.date" % months)
    return query
	
def get_all_old_dates():
    query = query_database("SELECT date from eventdb.events where events.date < CURDATE()")
    return query

def update_database(query):
    db = MySQLdb.connect(db_server, db_user, db_password, default_table)
    cursor = db.cursor()
    try:
       cursor.execute(query)
       db.commit()
    except:
       db.rollback()
    db.close()

def update_old_dates_in_database_to_next_year():
    '''
    Any date older than today is updated to next year
    '''
    old_dates_list = get_all_old_dates()
    for oldDate in old_dates_list:
            oldDate = oldDate[0]
            newDate = str(oldDate)
            oldYear = str(oldDate.strftime("%Y"))
            print "Old year=", oldYear
            newYear = str(datetime.datetime.now().year+1)
            print "New Year=", newYear
            newDate = newDate.replace(oldYear, newYear, 1)
            query = "UPDATE eventdb.events SET events.date='%s' WHERE events.date='%s' AND events.recurring=1" %(newDate,oldDate)
            print query
            update_database(query)

def get_birth_year(name):
    query = query_database("SELECT year FROM eventdb.events WHERE eventName = \"%s\"" % name)
    return query
    
def query_config_database(query):
    db = MySQLdb.connect('localhost','root','neerg42','dashdb')
    cursor = db.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result
    db.close()
