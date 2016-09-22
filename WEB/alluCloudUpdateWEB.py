#!/usr/bin/python

'''
Updates HTML file on WWW server with current data from WEB module
'''

import os
import datetime
import alluCloudCommunicationWEB
import urllib2

##Get file
alluCloudCommunicationWEB.get_index_html_from_allu_cloud_WEB_by_HTTP()

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
#SCAN WEB PAGES
f = open('index.html','r')
n = open('indexnew.html','w')

def get_webpage(URL):
    u = urllib2.urlopen(URL)
    localFile = open('page.html', 'w')
    localFile.write(u.read())
    localFile.close()

##get urls
allUrls = alluCloudCommunicationWEB.get_urls()
pages = []

##add some customized URLs
pages.append("http://www.telkku.com/programtable/show/0/" + (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y%m%d"))
pages.append("http://www.telkku.com/programtable/show/1/" + (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y%m%d"))
pages.append("http://www.telkku.com/programtable/show/0/" + (datetime.datetime.now() + datetime.timedelta(days=2)).strftime("%Y%m%d"))
pages.append("http://www.telkku.com/programtable/show/1/" + (datetime.datetime.now() + datetime.timedelta(days=2)).strftime("%Y%m%d"))
pages.append("http://www.telkku.com/programtable/show/0/" + (datetime.datetime.now() + datetime.timedelta(days=3)).strftime("%Y%m%d"))
pages.append("http://www.telkku.com/programtable/show/1/" + (datetime.datetime.now() + datetime.timedelta(days=3)).strftime("%Y%m%d"))
pages.append("http://www.telkku.com/programtable/show/0/" + (datetime.datetime.now() + datetime.timedelta(days=4)).strftime("%Y%m%d"))
pages.append("http://www.telkku.com/programtable/show/1/" + (datetime.datetime.now() + datetime.timedelta(days=4)).strftime("%Y%m%d"))
for url in allUrls:
    pages.append(url[1])

##get strings
allStrings = alluCloudCommunicationWEB.get_strings()
strings = []
for eachString in allStrings:
    strings.append(eachString[1])
for line in f.readlines():
    if "Website hits..." in line:
        n.write(line)
        for page_name in pages:
            print page_name
            get_webpage(page_name)
            f = open('page.html','r')
            
            counter = 0
            for line in f.readlines():
                for str in strings:
                    if str.upper() in line.upper():
                        n.write("<b>\"%s\"</b> found on webpage:<a href=%s>%s</a><br>" %(str,page_name,page_name))
                        counter = 1
    else:
        n.write(line)

f.close()
n.close()
os.remove('index.html')
os.rename('indexnew.html','index.html')


###Modify file
#WEB STATS
f = open('index.html','r')
n = open('indexnew.html','w')

string_count = alluCloudCommunicationWEB.count_all_strings()
url_count = alluCloudCommunicationWEB.count_all_urls()

for line in f.readlines():
    if "Web stats" in line:
        n.write(line)
        n.write("Database contains %s strings and " % string_count[0])
        n.write("%s webpages.<br>" % url_count[0])
    else:
        n.write(line)

f.close()
n.close()
os.remove('index.html')
os.rename('indexnew.html','index.html')

###Upload it again
alluCloudCommunicationWEB.send_file_to_allu_cloud_WEB_by_FTP('index.html')
