#!/bin/python
import MySQLdb
import datetime
# Open database connection
db = MySQLdb.connect("localhost","otrs","BN#2018PL","otrs" )
# prepare a cursor object using cursor() method
cursor = db.cursor()
sql = "SELECT * FROM `ticket_number_counter` ORDER BY `create_time` DESC"
# Execute the SQL command
cursor.execute(sql)
# Fetch all the rows in a list of lists.
results = cursor.fetchone()
id = results[0]
counter = results[1]
counter_uid = results[2]
create_time = results[3]
# disconnect from server
db.close()
from time import strftime
now=strftime("%Y-%m-%d %H:%M:%S")
from datetime import datetime
from datetime import date
tickettime=datetime.strptime(str(results[3]), "%Y-%m-%d %H:%M:%S")
current=datetime.strptime(str(now), "%Y-%m-%d %H:%M:%S")
to = current - tickettime
diff=int(to.total_seconds())
if diff <= 10:
        print "OTRS is working"
else:
        print "OTRS is not working since %s" %tickettime
