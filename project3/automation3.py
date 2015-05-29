import sys
import os

def calltcl(time_interval,tcpvariant1):
# execfile(ns project3.tcl tcpvariant cbr)
# execfile(python parse_trace.py)
	os.system("ns project33.tcl "+tcpvariant1+" "+str(float(time_interval)))
	os.system("python parse_latency.py")

def executetcl():
	time_interval = 1
	while (time_interval < 25):
		calltcl(time_interval,"TCP/Reno")
		time_interval = time_interval + 1


executetcl()
