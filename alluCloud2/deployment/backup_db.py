#!/usr/bin/env python

import os
import time

db_user = 'root'
db_password = 'alluCloudPassword'

os.popen("mysqldump -u %s -p%s eventdb events eventtypes > deployment\db_backups\%s.sql" % (db_user,db_password,"eventsdb1"))