#!/usr/bin/env python
#
#  Mattias Hemmingsson
#  matte@elino.se
#
# Script for rescricting nagios messages
# Only send one sms / email and then paus for some time.
# This for not flouding sms system while system reboot 
# 
import csv
import time
import datetime
import os.path, time
from time import gmtime, strftime, mktime
import smtplib
import sys

def send_email(to,message):
	'''
	Sending the email.
	'''

	sender = 'syco-norely@fareoffice.com'
	
	try:
		smtpObj = smtplib.SMTP('mail.fareoffice.com')
		smtpObj.sendmail(sender, to, message)         
		print "Successfully sent email"
	except SMTPException:
		print "Error: unable to send email"

def save_to_file(to,message,host):
  '''
  Saves the oncall to file
  '''
  f = open(to+".txt", "w")
  f.write(to+","+host)
  f.close()


def is_message_sent(to,message,host):
 	'''
 	Cheks if teh message has bean sent before
 	'''
	 
	
	#print strftime("%Y-%m-%d %H:%M:%S",os.path.getmtime(to + '.txt'))
	#print time.mktime(time.gmtime())
	
	try:
		with open(to + '.txt', 'rb') as f:
			diffrent = time.time() - os.path.getmtime(to + '.txt')
			print diffrent
			reader = csv.reader(f)
			for row in reader:
				if diffrent < 3600:
					return True
				else:
					return False
	except IOError:
		return False
def incomming(to,message,host):
	'''
	Incomming messages
	'''
	#Has en sms bean send the latest our
	if is_message_sent(to,message,host):
		print "Sending to gmail"
		send_email('matte.hemmingsson@gmail.com',message)
	else:
		print "Seding to sms"

		#Sending to sms
		send_email(to,message)

		
		#Saving message to file
		save_to_file(to,message,host)



if len(sys.argv) ==5:
	print 'Argument List:', str(sys.argv)
	headers = ["from: noreply@fareoffice.com",
           "subject: SYCO",
           "to: " + sys.argv[4],
           "mime-version: 1.0",
           "content-type: text/html"]
	headers = "\r\n".join(headers)

	messages="""{0}{1}

	""".format(sys.argv[1],sys.argv[3])
	incomming(sys.argv[4],headers+"\r\n\r\n"+ messages,sys.argv[2])
else:
	print "Error number of arguments please use './sms_send.py hoststate hostalias message contactemail'" 

