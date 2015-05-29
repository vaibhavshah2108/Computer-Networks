

trace_file= open('project333.tr','r')
count = 0
variant1_count = 0
variant2_count = 0
pcount1 = 0
pcount2 = 0
source = '2'
destination = '3' 
total_size_1 = 0.0
source_addr = '0.0'
dest_addr = '3.0'
source_1 = '2'
destination_1 = '5'
source_addr1 = '4.0'
dest_addr1 = '5.0'
total_size_2 = 0.0
latency_dict = {}
total_latency = 0.0
total_latency_in = 0.0
total_latency_two = 0
latency_dict1 = {}
for row in trace_file:
	row = row.split()


	#Calculation of Throughput
	if row[0] == '-' and row[7] == '1' and row[2] == source and row[3] == destination and row[8] == source_addr and row[9] == dest_addr:
                total_size_1 = total_size_1 + float(8 * float(row[5])/ 10**6)
                #pcount1 = pcount1 + 1
        time_field1 = float(row[1])

        if row[0] == '-' and row[7] == '2' and row[2] == source_1 and row[3] == destination_1 and row[8] == source_addr1 and row[9] == dest_addr1:
                total_size_2 = total_size_2 + float(8 * float(row[5])/ 10**6)
                #pcount2 = pcount2 + 1
        time_field2 = float(row[1])



	#Calculation of Latency
	if row[0] == '-' and row[7] == '1' and row[2] == '0' and row[3] == '1' and row[8] == source_addr and row[9] == dest_addr:
                if row[11] not in latency_dict:
#			print " 1st if"
                        latency_dict[row[11]] = float(row[1])		
                        #print "dict:",latency_dict

        if row[0] == '-' and row[7] == '1' and row[2] == source and row[3] == destination and row[8] == source_addr and row[9] == dest_addr:                 
                if row[11] in latency_dict:                      
#			print " 2nd if"
			#print "Subtracting % from %",(latency_dict[row[11]],row[1])
                        latency_dict[row[11]] = float(row[1]) - latency_dict[row[11]]
			#total_latency_in = total_latency_in + float(row[1]) - latency_dict[row[11]]

	if row[0] == '-' and row[7] == '2' and row[2] == '4' and row[3] == '1' and row [8] == '4.0' and row[9] == '5.0':
		if row[11] not in latency_dict1:
#			print " 3rd if"
			latency_dict1[row[11]] = float(row[1])

	if row[0] == '-' and row[7] == '2' and row[2] == source and row[3] == '5' and row[8] == '4.0' and row[9] == '5.0':
		if row[11] in latency_dict1:
#			print " 4th if"
			latency_dict1[row[11]] = float (row[1]) - latency_dict1[row[11]]
			#total_latency_in = total_latency_in + (float(row[1]) - latency_dict1[row[11]]


	#Calculation of drop
	if row[0] == 'd' and row[4] == "tcp" and row[7] == '1':
                variant1_count = variant1_count + 1
                #print "Drops from this variant1:",variant1_count

        if row[0] == 'd' and row[4] == "cbr" and row[7] == '2':
                variant2_count = variant2_count + 1

	




#print "Drop1: ",variant1_count
#print "Drop2: ",variant2_count

for key in latency_dict:
        total_latency+=latency_dict[key]

latency = total_latency/len(latency_dict)
			
for key in latency_dict1:
	total_latency_two+=latency_dict1[key]

latency_1 = 0
if len(latency_dict1) > 0:
	latency_1 = total_latency_two/len(latency_dict1)

#count = variant1_count + variant2_count
#print "Packets dropped for variant_1:		", variant1_count
#print "Packets dropped for varian_2:		", variant2_count 
#print "Total packet drop:",count
throughput_1 = total_size_1/time_field1
#print "Throughput for variant_1:		",throughput_1
throughput_2 = total_size_2/time_field2
#print "Throughput for variant_2:		",throughput_2
with open("throughput1.txt", "a") as exp3_throughput1:
    exp3_throughput1.write(str(throughput_1)+'\n')
with open("throughput2.txt", "a") as exp3_throughput2:
    exp3_throughput2.write(str(throughput_2)+'\n')
#with open("drop1.txt", "a") as variant1_drop:
#    variant1_drop.write(str(variant1_count)+'\n')
#with open("drop2.txt", "a") as variant2_drop:
#    variant2_drop.write(str(variant2_count)+'\n')
with open("latency1.txt","a") as exp3_latency:
    exp3_latency.write(str(latency)+'\n')
with open("latency2.txt","a") as exp3_latency2:
    exp3_latency2.write(str(latency_1)+'\n')

#print "latency1",latency
#print "latency2",latency_1
#print "time",time_field 
#print "Number of packets dropped:    ", count
#print "Number of packets dropped:",count	
#print "Total size of packets:",total_size
#throughput = total_size/time_field
'''
with open("throughput.txt", "a") as myfile:
    myfile.write(str(throughput)+'\n')
print "Packet count", pcount
print "Throughput:	",throughput
'''
