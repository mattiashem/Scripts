#!/usr/bin/env python

import socket
import dns.resolver

#v="yes"
g_dns="88.80.170.189"
o_dns="81.201.209.55"








def test_dns(name,typ,v):
	print "==================================================================="
	try:
		answers = dns.resolver.query(name,typ )
		for rdata in answers:
			if v =="yes":
				print "Your DNS = " + str(rdata)
	except dns.exception.DNSException as e:
		if isinstance(e, dns.resolver.NXDOMAIN):
			print "ERROR Domain " +name+ " Not in server LOCAL"
			rdata="NO"
		

	resolver_g = dns.resolver.Resolver()
	resolver_g.nameservers = [g_dns]
	try:
		for rdata_g in resolver_g.query(name, typ) :
		  if v =="yes":
		    print "Telecity DNS = " + str(rdata_g)
		
	except dns.exception.DNSException as e:
		if isinstance(e, dns.resolver.NXDOMAIN):
			print "ERROR Domain " +name+ " Not in server TeleCity\n"
			rdata_g="NO"
	
	resolver_o = dns.resolver.Resolver()
	resolver_o.nameservers = [o_dns]
	try:
		for rdata_o in resolver_o.query(name, typ) :
		    if v =="yes":
		    	print "Avalio DNS = " + str(rdata_o)
	except dns.exception.DNSException as e:
		if isinstance(e, dns.resolver.NXDOMAIN):
			print "ERROR Domain " +name+ " Not in server Avalio\n"
			rdata_o="NO"


	if rdata == rdata_g and rdata == rdata_o:
		if v =="yes":
			print "OK " + name + " = " + str(rdata)+"\n"
	
	else:
		print "CRITICAL " + name + " NOT SAME ON ALL SERVERS" +"\n"



def test_cname(cname,v):
	try:
		answers = dns.resolver.query(cname,"CNAME" )
		for rdata in answers:
			if v =="yes":
				print "###########DNAME "+cname+"-->"+str(rdata)+" #################\n"
			test_dns(str(rdata),"A","yes")
	except dns.exception.DNSException as e:
		if isinstance(e, dns.resolver.NXDOMAIN):
			print "ERROR CNAME dont exsist in server"+cname
			rdata="NO"



f = open('dns_name.txt')
for line in iter(f):
	line = line.replace('\n','')
	name = line.split(' ')
	if name[0]=="CNAME":
		test_cname(name[1],"yes")
	if name[0]=="A":
		test_dns(name[1],name[0],"yes")
f.close()
	
