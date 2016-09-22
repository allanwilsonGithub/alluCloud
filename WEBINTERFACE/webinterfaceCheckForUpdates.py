import os
import ftplib
from ftplib import FTP
import CONSOLE.console_actions_notes
import shutil
import logging
logging.basicConfig(filename="D:\\ALLUSTORE\\alluCloud\\alluCloud.log",level=logging.DEBUG)

QNAPserver = "192.168.100.200"
QNAPUser = "alluCloud"
QNAPPass = "alluCloudPassword"
QNAPDir = "Qweb/alluCloud/filesToProcess"
localDir = "d:\\ALLUSTORE\\alluCloud\\WEBINTERFACE\\workingDirectory\\"

#Remove and recreate working dir
try:
    shutil.rmtree(localDir)
except:
    logging.warning('Problem removing workingDirectory for WEBINTERFACE') 
try:
    os.makedirs(localDir)
except:
    logging.warning('Problem creating workingDirectory for WEBINTERFACE')

#FTP get the files
ftp = FTP(QNAPserver)
ftp.login(QNAPUser,QNAPPass)
ftp.cwd(QNAPDir)

filenames = []
ftp.retrlines('NLST', filenames.append)

for filename in filenames:
    local_filename = os.path.join(localDir, filename)
    file = open(local_filename, 'wb')
    ftp.retrbinary('RETR '+ filename, file.write)
    file.close()
    ftp.delete(filename)

ftp.close()

#Get inputs per file
newNotes = []
newEvents = []
for file in filenames:
    f = open(localDir + file,'r')
    lines = f.readlines()
    for line in lines:
        line = line.rstrip()
        if 'NewNote' in line:
            NewNoteOutput = line.split(":")
            newNotes.append(NewNoteOutput[1])
        if 'NewEvent' in line:
            NewEventOutput = line.split(":")
            newEvents.append(NewEventOutput[1])
    f.close()

#Add to DB
for note in newNotes:
##    try:
        CONSOLE.console_actions_notes.add_note(note)
##    except:
##        print "Failed to add new note using console_action_notes."
