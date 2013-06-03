#!/usr/bin/env python

#
# Script for testing ossec logs.
# tries to loggin on server wirh woring password 
# that will generat en log on the host sent to ossec and then
# ossec will alert on the login attempt


import paramiko




def ssh_in(host):
	'''
	ssh in to host with user and pass
	'''

	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	try:
		ssh.connect(hostname=host, username='HACKER', password='XXXX')
		ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('df -h')
		print ssh_stdout.readlines()
	except Exception, e:
		print "Error"




f = open('hosts.txt')
for line in iter(f):
	line = line.replace('\n','')
	host = line.split(' ')
	print "SSH into host"+host[0]
	ssh_in(host[0])
f.close()



