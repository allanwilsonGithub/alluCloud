#!/usr/bin/python

'''
Updates HTML file on WWW server with current data from EVENT module
'''

import os
import datetime
import alluCloudCommunicationEVENT



monthsToShow = 12
sendEmail = 1

###SETUP EMAIL TEXT
emailText = []

##Update EVENT dates
alluCloudCommunicationEVENT.update_old_dates_in_database_to_next_year()


#Modify file
#LAST UPDATE
f = open('D:\\ALLUSTORE\\alluCloud\\EVENT\\indexTemplate.html', 'r')
n = open('indexnew.html','w')

for line in f.readlines():
    if "Last update..." in line:
        n.write("Updated: " + datetime.datetime.now().strftime("%A %d/%m/%Y %H:%M"))
        emailText.append("Updated: " + datetime.datetime.now().strftime("%A %d/%m/%Y %H:%M"))
    elif "Day:" in line or "Date:" in line or "Time:" in line:
        pass
    else:
        n.write(line)

f.close()
n.close()
os.rename('indexnew.html','index.html')

#Modify file
#List events
f = open('index.html','r')
n = open('indexnew.html','w')

events_list = alluCloudCommunicationEVENT.list_events(monthsToShow)
emailText.append("===============================")
for line in f.readlines():
    if "Event Type" in line:
        n.write("<B><U>" + datetime.datetime.now().strftime("%A %d/%m/%Y") + "</B></U>")
        n.write(line)
        a = 0
        for l in events_list:
            if events_list[a][3]=="Birthday":
                fontColour="66AA00"
            elif events_list[a][3]=="Task":
                fontColour="66AACC"
            elif events_list[a][3]=="PublicEvent":
                fontColour="CC6633"
            elif events_list[a][3]=="Reminder":
                fontColour="yellow"
            else:
                fontColour="9933CC"
            diffYear=int((events_list[a][0]).strftime("%Y"))
            diffMonth=int((events_list[a][0]).strftime("%m"))
            diffDay=int((events_list[a][0]).strftime("%d"))
            days_to_go = (datetime.date(diffYear,diffMonth,diffDay) - datetime.date.today()).days
            if days_to_go==0:
                days_to_go="Today"

            ###AGE##########
            birth_year = alluCloudCommunicationEVENT.get_birth_year(events_list[a][1])
            birthYear = int(birth_year[0][0])
            from_date=datetime.date(birthYear,diffMonth,diffDay)
            to_date=datetime.date.today()
            leap_day_anniversary_Feb28=True
            age = to_date.year - from_date.year
            try:
                anniversary = from_date.replace(year=to_date.year)
            except ValueError:
                assert from_date.day == 29 and from_date.month == 2
                if leap_day_anniversary_Feb28:
                    anniversary = datetime.date(to_date.year, 2, 28)
                else:
                    anniversary = datetime.date(to_date.year, 3, 1)
            if to_date < anniversary:
                age -= 1
            if age <0:
                age = ""
            ################


            n.write("<tr BGCOLOR=\"%s\"><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % (fontColour,days_to_go,events_list[a][1],events_list[a][2],age,events_list[a][0],events_list[a][3]))
            emailText.append("%s days to go...     %s     %s   %s     %s     %s" % (days_to_go,events_list[a][1],events_list[a][2],events_list[a][0],events_list[a][3],age))
            a = a+1
    else:
        n.write(line)

f.close()
n.close()
os.remove('index.html')
os.rename('indexnew.html','index.html')

###Modify file
#Count all events
f = open('index.html','r')
n = open('indexnew.html','w')

events_count = alluCloudCommunicationEVENT.count_all_events()

for line in f.readlines():
    if "Event total" in line:
        n.write(line)
        n.write("Number of events in database: %s <br>" % events_count[0])
        emailText.append("===============================")
        emailText.append("Number of events in database: %s" % events_count[0])
    else:
        n.write(line)

f.close()
n.close()
os.remove('index.html')
os.rename('indexnew.html','index.html')

###EMAIL######################
str_list = []
for n in emailText:
    str_list.append(n)
    str_list.append("\n")
textToMail = ''.join(str_list)

if sendEmail == 1:
    alluCloudCommunicationEVENT.send_mail(str(textToMail))
##########################
