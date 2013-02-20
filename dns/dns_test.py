#!/usr/bin/env python

import socket
import dns.resolver

#v="yes"
g_dns="8.8.8.8"
o_dns="208.67.222.222"








def test_dns(name,typ,v):
	answers = dns.resolver.query(name,typ )
	for rdata in answers:
	  if v =="yes":
	    print "Your DNS = " + str(rdata)
		
	resolver_g = dns.resolver.Resolver()
	resolver_g.nameservers = [g_dns]
	for rdata_g in resolver_g.query(name, typ) :
	  if v =="yes":
	    print "Google DNS = " + str(rdata_g)
	
	
	resolver_o = dns.resolver.Resolver()
	resolver_o.nameservers = [o_dns]
	for rdata_o in resolver_o.query(name, typ) :
	    if v =="yes":
	    	print "OpenDNS DNS = " + str(rdata_o)
	
	if rdata == rdata_g and rdata == rdata_o:
		if v =="yes":
			print "OK " + name + " = " + str(rdata)
	
	else:
		print "CRITICAL" + name + " = " + str(rdata) 


f = open('dns_name.txt')
for line in iter(f):
	line = line.replace('\n','')
	name = line.split(' ')
	test_dns(name[0],name[1],"yes")
f.close()
	
