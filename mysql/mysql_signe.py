#!/usr/bin/env python

#Script for adding user to mysql.
#Based on date.

from datetime import timedelta,date

def signed():
	startdate= date.today() - timedelta(154)
	
	while startdate != date.today():
		print "insert into signed(date,sign,mess,signdate) VALUES('"+str(startdate)+"','mathem','message','"+ str(startdate + timedelta(1))+"');"
		
		startdate = startdate + timedelta(1)


signed()
