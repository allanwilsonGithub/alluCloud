#!/usr/bin/python

'''
Connections between cloud parts (FTP, MYSql, HTTP) for TOTALBACKUP module
'''

import urllib2
import ftplib
from ftplib import FTP

#Get variables from config file
import ConfigParser
config = ConfigParser.ConfigParser()
config.read("d:\\ALLUSTORE\\alluCloud\\alluCloud.conf")

PathToTotalBackupHTTPIndexTemplate = config.get('TOTALBACKUP', 'PathToTotalBackupHTTPIndexTemplate')
FTPTotalBackupDir = config.get('TOTALBACKUP', 'FTPTotalBackupDir')
FtpServer = config.get('FTP', 'FtpServer')
FTPUser = config.get('FTP', 'FTPUser')
FTPPass = config.get('FTP', 'FTPPass')

#####HTTP
def get_index_html_from_allu_cloud_TOTALBACKUP_by_HTTP():
    u = urllib2.urlopen(PathToTotalBackupHTTPIndexTemplate)
    localFile = open('index.html', 'w')
    localFile.write(u.read())
    localFile.close()

###FTP
def send_file_to_allu_cloud_TOTALBACKUP_by_FTP(filename):
    ftp = FTP(FtpServer)
    ftp.login(FTPUser,FTPPass)
    ftp.cwd(FTPTotalBackupDir)
    ftp.storlines("STOR " + filename, file(filename, "rb"))
    ftp.quit()