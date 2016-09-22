#!/usr/bin/python

'''
Updates HTML file on WWW server with current data from TOTALBACKUP module
'''

import os
import datetime
import alluCloudCommunicationTOTALBACKUP
import totalbackup

##Get files
alluCloudCommunicationTOTALBACKUP.get_index_html_from_allu_cloud_TOTALBACKUP_by_HTTP()
l = open('D:\\ALLUSTORE\\alluCloud\\alluCloud.log','r')


#Modify file
#LAST UPDATE
f = open('index.html','r')
n = open('indexnew.html','w')

for line in f.readlines():
    if "Last update..." in line:
        n.write("Updated: " + datetime.datetime.now().strftime("%A %d/%m/%Y %H:%M"))
    elif "Day:" in line or "Date:" in line or "Time:" in line:
        pass
    else:
        n.write(line)

f.close()
n.close()
os.remove('index.html')
os.rename('indexnew.html','index.html')

###Modify file
#Count titles
f = open('index.html','r')
n = open('indexnew.html','w')

for line in f.readlines():
    if "TotalBackup Status" in line:
        n.write(line)
        flag = 0
        for line in l:
            now = datetime.datetime.now()
            d = now.date()
            if str(d) in line and "TotalBackup: " in line and "AlluCloudTotalBackup stopped" not in line and "No changes since zip was created" not in line and "Backup directory" not in line and "Zip is updated when changes are" not in line:
                n.write(line)
                n.write("<br>")

    else:
        n.write(line)

f.close()
n.close()
os.remove('index.html')
os.rename('indexnew.html','index.html')


###Upload it again
alluCloudCommunicationTOTALBACKUP.send_file_to_allu_cloud_TOTALBACKUP_by_FTP('index.html')
