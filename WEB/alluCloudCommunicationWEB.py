#!/usr/bin/python

'''
Connections between cloud parts (FTP, MYSql, HTTP) for web module
'''

import urllib2
import ftplib
from ftplib import FTP
import MySQLdb

#Get variables from config file
import ConfigParser
config = ConfigParser.ConfigParser()
config.read("d:\\ALLUSTORE\\alluCloud\\alluCloud.conf")

PathToWebHTTPIndexTemplate = config.get('WEB', 'PathToWebHTTPIndexTemplate')
FTPWebDir = config.get('WEB', 'FTPWebDir')
MYSQLPass = config.get('MySQL', 'MYSQLPass')
FtpServer = config.get('FTP', 'FtpServer')
FTPUser = config.get('FTP', 'FTPUser')
FTPPass = config.get('FTP', 'FTPPass')


#####HTTP
def get_index_html_from_allu_cloud_WEB_by_HTTP():
    u = urllib2.urlopen(PathToWebHTTPIndexTemplate)
    localFile = open('index.html', 'w')
    localFile.write(u.read())
    localFile.close()

###FTP
def send_file_to_allu_cloud_WEB_by_FTP(filename):
    ftp = FTP(FtpServer)
    ftp.login(FTPUser,FTPPass)
    ftp.cwd(FTPWebDir)
    ftp.storlines("STOR " + filename, file(filename, "rb"))
    ftp.quit()

### MYSQL
LOCAL_ENV = ['localhost','root',MYSQLPass,'webdb']
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

def get_urls():
    query = query_database("SELECT * FROM webdb.urls")
    return query

def get_strings():
    query = query_database("SELECT * FROM webdb.searchstrings")
    return query

def count_all_urls():
    query = query_database("SELECT count(url) FROM webdb.urls")
    return query

def count_all_strings():
    query = query_database("SELECT count(string) FROM webdb.searchstrings")
    return query
