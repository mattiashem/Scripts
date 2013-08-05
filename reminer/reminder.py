#!/usr/bin/env python
#
#  Mattias Hemmingsson
#  matte@elino.se
#
# Script for reminder friend when to bet
# Uses and csv file and send email to remind when its time to bet.
#
# 
import csv
import smtplib
from datetime import datetime, timedelta, date



#Get users and send email to users
sender = 'noreply@elino.se'
emails =[]
better = ""
week = 2

def save_to_file(name):
  '''
  Saves the oncall to file
  '''
  f = open("oncall.txt", "w")
  f.write(name)
  f.close()


def read_file():
  '''
  read the oncall to file
  '''
  f = open("oncall.txt", "r")
  return int(f.readline()) + 1
  f.close()


def send_oncall():
    '''
    Send an reminder ho is oncall
    '''

    #Get cont on oncall staff and next oncall
    numeroncall =  str(int(len(open("people.csv").readlines())) +1)
    nextoncall = str(read_file())
    
    
    #Loop to begning of file 
    if nextoncall == numeroncall:
      nextoncall = '1'
      
    #Send email to oncall staff
    emails=[]

    #Get how is oncall
    with open('people.csv', 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            emails.append(row[2])
            if row[0] == nextoncall:
              oncall = row[1]
              #Save oncall to file
              save_to_file(row[0])

        
    
    
    
    message = """From: SYCO <noreply@fareoffice.com>
    To: SYSOP
    Subject: {0} IS NOW ONCALL
    
    This is an reminder that {0} is now oncall.
    """.format(oncall)

    send_email(emails,message)


def weekly():
  '''
  Script to run every week to remind to update week report and
  to update docs in redmine
  '''
  message = """Subject:Weekly checks on syco systems\N
                        \n
                        \n
                        Dokument\n
                        Complete weekly notes in redmine in this link https://redmine.fareoffice.com/projects/policy/wiki/{0}v{1} \n
                        Use the template here to https://redmine.fareoffice.com/projects/policy/wiki/Weekly_activities \n
                        And add the notes to the redmine.\n
                        \n
                        \n
                        Updates\n
                        Verify that we have the latest version of the software from this page\n
                        https://redmine.fareoffice.com/projects/policy/wiki/Monthly_activities \n
                        Of new update is found start CHANGE MAN\n
                        \n
            """.format(date.today().year,datetime.today().isocalendar()[1])
  send_email("sysop@fareoffice.com",message)

def quartly():
  '''
  Script to remind the qyartely tasks
  '''
  message = """From: From Herrklubben <from@fromdomain.com>
            To: Grabbarna 
            Subject: {0} Glom inte att betta"""

#Sending the email
def send_email(emails,message):
      sender = "sycoreply@elino.se"
      '''
      Send the email
      '''
      
      try:
         smtpObj = smtplib.SMTP('localhost')
         smtpObj.sendmail(sender, emails, message)         
         print "Successfully sent email"
      except SMTPException:
         print "Error: unable to send email"
      
      print emails
      print sender + message   

send_oncall()
#weekly()