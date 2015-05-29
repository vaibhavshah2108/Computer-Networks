

trace_file = open('project33.tr','r')
count = 0
pcount = 0
source = '2'
destination = '3' 
total_size = 0.0
source_addr = '0.0'
dest_addr = '3.0'
latency_dict = {}
total_latency = 0

for row in trace_file:
	row = row.split()
	if row[0] == '-' and row[7] == '1' and row[2] == source and row[3] == destination and row[8] == source_addr and row[9] == dest_addr:		
                total_size = total_size + float(8 * float(row[5])/ 10**6)           
		pcount = pcount + 1
	time_field = float(row[1])
		
	if row[0] == 'd' and row[4] == "tcp":
		count = count + 1	
	
	if row[0] == '-' and row[7] == '1' and row[2] == '0' and row[3] == '1' and row[8] == source_addr and row[9] == dest_addr:
		if row[11] not in latency_dict:			
			latency_dict[row[11]] = float(row[1])
			#print "dict:",latency_dict
	
	if row[0] == '-' and row[7] == '1' and row[2] == source and row[3] == destination and row[8] == source_addr and row[9] == dest_addr:						
		if row[11] in latency_dict:
			#print "Subtracting % from %",(latency_dict[row[11]],row[1])
			latency_dict[row[11]] = float (row[1]) - latency_dict[row[11]]
						
	

for key in latency_dict:
	total_latency+=latency_dict[key]


#print "total latency:", total_latency
#print "unique_keys:",len(latency_dict)
latency = total_latency/len(latency_dict)
#print "the total end to end latency is :",latency
#print "time",time_field 
print "Number of packets dropped:    ", count
#print "Number of packets dropped:",count	
#print "Total size of packets:",total_size
throughput = total_size/time_field
with open("throughput.txt", "a") as myfile:
    	myfile.write(str(throughput)+'\n')
with open("packetdrop.txt","a") as myfile1:
    	myfile1.write(str(count)+'\n')
with open("latency1.txt","a") as myfile2:
	myfile2.write(str(latency)+'\n')
#print "Packet count", pcount
print "Throughput:	",throughput
