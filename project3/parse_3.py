trace_file= open('project333.tr','r')
variant1_count = 0
variant2_count = 0
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
total_latency = 0
total_latency_two = 0
latency_dict1 = {}
total_size_13 = 0.0
total_size_14 = 0.0 
total_size_15 = 0.0 
total_size_16 = 0.0 
total_size_17 = 0.0
total_size_18 = 0.0 
total_size_19 = 0.0
total_size_10 = 0.0
total_size_11 = 0.0
total_size_12 = 0.0
total_size_20 = 0.0
total_size_21 = 0.0
total_size_22 = 0.0
total_size_23 = 0.0
total_size_24 = 0.0
total_size_25 = 0.0

for row in trace_file:
        row = row.split()
        #Calculation of Throughput
	if row[1]:
		time = float(row[1])
		
		if time >=9.0 and time <=10.0:
                        if row[0] == 'r' and row[7] == '2' and row[2] == '2' and row[3] == '5' and row[8] == '4.0' and row[9] == '5.0' and row[4] == "cbr":
                                total_size_10 = total_size_10 + float(8 * float(row[5])/ 10**6)
                                #pcount1 = pcount1 + 1
                                time_field10 = float(row[1])
                                throughput10 = total_size_10/time_field10
                                with open("throughput3e10.txt", "a") as throughput_exp3:
                                        throughput_exp3.write(str(throughput10)+'\n')

		if time >=10.0 and time <=11.0:
                        if row[0] == 'r' and row[7] == '2' and row[2] == '2' and row[3] == '5' and row[8] == '4.0' and row[9] == '5.0' and row[4] == "cbr":
                                total_size_11 = total_size_11 + float(8 * float(row[5])/ 10**6)
                                #pcount1 = pcount1 + 1
                                time_field11 = float(row[1])
                                throughput11 = total_size_11/time_field11
                                with open("throughput3e11.txt", "a") as throughput_exp3:
                                        throughput_exp3.write(str(throughput11)+'\n')
	
		if time >=11.0 and time <=12.0:
                        if row[0] == 'r' and row[7] == '2' and row[2] == '2' and row[3] == '5' and row[8] == '4.0' and row[9] == '5.0' and row[4] == "cbr":
                                total_size_12 = total_size_12 + float(8 * float(row[5])/ 10**6)
                                #pcount1 = pcount1 + 1
                                time_field12 = float(row[1])
                                throughput12 = total_size_12/time_field12
                                with open("throughput3e12.txt", "a") as throughput_exp3:
                                        throughput_exp3.write(str(throughput12)+'\n')
		
	
		if time >=12.0 and time <=13.0:
                        if row[0] == 'r' and row[7] == '2' and row[2] == '2' and row[3] == '5' and row[8] == '4.0' and row[9] == '5.0' and row[4] == "cbr":
                                total_size_13 = total_size_13 + float(8 * float(row[5])/ 10**6)
                                #pcount1 = pcount1 + 1
                                time_field13 = float(row[1])
                                throughput13 = total_size_13/time_field13
                                with open("throughput3e13.txt", "a") as throughput_exp3:
                                        throughput_exp3.write(str(throughput13)+'\n')

		if time >=13.0 and time <=14.0:
                        if row[0] == 'r' and row[7] == '2' and row[2] == '2' and row[3] == '5' and row[8] == '4.0' and row[9] == '5.0' and row[4] == "cbr":
                                total_size_14 = total_size_14 + float(8 * float(row[5])/ 10**6)
                                #pcount1 = pcount1 + 14
                                time_field14 = float(row[1])
                                throughput14 = total_size_14/time_field14
                                with open("throughput3e14.txt", "a") as throughput_exp3:
                                        throughput_exp3.write(str(throughput14)+'\n')

		if time >=14.0 and time <=15.0:
                        if row[0] == 'r' and row[7] == '2' and row[2] == '2' and row[3] == '5' and row[8] == '4.0' and row[9] == '5.0' and row[4] == "cbr":
                                total_size_15 = total_size_15 + float(8 * float(row[5])/ 10**6)
                                #pcount1 = pcount1 + 14
                                time_field15 = float(row[1])
                                throughput15 = total_size_15/time_field15
                                with open("throughput3e15.txt", "a") as throughput_exp3:
                                        throughput_exp3.write(str(throughput15)+'\n')

		if time >=15.0 and time <=16.0:
                        if row[0] == 'r' and row[7] == '2' and row[2] == '2' and row[3] == '5' and row[8] == '4.0' and row[9] == '5.0' and row[4] == "cbr":
                                total_size_16 = total_size_16 + float(8 * float(row[5])/ 10**6)
                                #pcount1 = pcount1 + 14
                                time_field16 = float(row[1])
                                throughput16 = total_size_16/time_field16
                                with open("throughput3e16.txt", "a") as throughput_exp3:
                                        throughput_exp3.write(str(throughput16)+'\n')

		if time >=16.0 and time <=17.0:
                        if row[0] == 'r' and row[7] == '2' and row[2] == '2' and row[3] == '5' and row[8] == '4.0' and row[9] == '5.0' and row[4] == "cbr":
                                total_size_17 = total_size_17 + float(8 * float(row[5])/ 10**6)
                                #pcount1 = pcount1 + 14
                                time_field17 = float(row[1])
                                throughput17 = total_size_17/time_field17
                                with open("throughput3e17.txt", "a") as throughput_exp3:
                                        throughput_exp3.write(str(throughput17)+'\n')

		if time >=17.0 and time <=18.0:
                        if row[0] == 'r' and row[7] == '2' and row[2] == '2' and row[3] == '5' and row[8] == '4.0' and row[9] == '5.0' and row[4] == "cbr":
                                total_size_18 = total_size_18 + float(8 * float(row[5])/ 10**6)
                                #pcount1 = pcount1 + 14
                                time_field18 = float(row[1])
                                throughput18 = total_size_18/time_field18
                                with open("throughput3e18.txt", "a") as throughput_exp3:
                                        throughput_exp3.write(str(throughput18)+'\n')

		if time >=18.0 and time <=19.0:
                        if row[0] == 'r' and row[7] == '2' and row[2] == '2' and row[3] == '5' and row[8] == '4.0' and row[9] == '5.0' and row[4] == "cbr":
                                total_size_19 = total_size_19 + float(8 * float(row[5])/ 10**6)
                                #pcount1 = pcount1 + 14
                                time_field19 = float(row[1])
                                throughput19 = total_size_19/time_field19
                                with open("throughput3e19.txt", "a") as throughput_exp3:
                                        throughput_exp3.write(str(throughput19)+'\n')

		if time >=19.0 and time <=20.0:
                        if row[0] == 'r' and row[7] == '2' and row[2] == '2' and row[3] == '5' and row[8] == '4.0' and row[9] == '5.0' and row[4] == "cbr":
                                total_size_20 = total_size_20 + float(8 * float(row[5])/ 10**6)
                                #pcount1 = pcount1 + 14
                                time_field20 = float(row[1])
                                throughput20 = total_size_20/time_field20
                                with open("throughput3e20.txt", "a") as throughput_exp3:
                                        throughput_exp3.write(str(throughput20)+'\n')

		if time >=20.0 and time <=21.0:
                        if row[0] == 'r' and row[7] == '2' and row[2] == '2' and row[3] == '5' and row[8] == '4.0' and row[9] == '5.0' and row[4] == "cbr":
                                total_size_21 = total_size_21 + float(8 * float(row[5])/ 10**6)
                                #pcount1 = pcount1 + 14
                                time_field21 = float(row[1])
                                throughput21 = total_size_21/time_field21
                                with open("throughput3e21.txt", "a") as throughput_exp3:
                                        throughput_exp3.write(str(throughput21)+'\n')

		if time >=21.0 and time <=22.0:
                        if row[0] == 'r' and row[7] == '2' and row[2] == '2' and row[3] == '5' and row[8] == '4.0' and row[9] == '5.0' and row[4] == "cbr":
                                total_size_22 = total_size_22 + float(8 * float(row[5])/ 10**6)
                                #pcount1 = pcount1 + 14
                                time_field22 = float(row[1])
                                throughput22 = total_size_22/time_field22
                                with open("throughput3e22.txt", "a") as throughput_exp3:
                                        throughput_exp3.write(str(throughput22)+'\n')

		if time >=22.0 and time <=23.0:
                        if row[0] == 'r' and row[7] == '2' and row[2] == '2' and row[3] == '5' and row[8] == '4.0' and row[9] == '5.0' and row[4] == "cbr":
                                total_size_23 = total_size_23 + float(8 * float(row[5])/ 10**6)
                                #pcount1 = pcount1 + 14
                                time_field23 = float(row[1])
                                throughput23 = total_size_23/time_field23
                                with open("throughput3e23.txt", "a") as throughput_exp3:
                                        throughput_exp3.write(str(throughput23)+'\n')

		if time >=23.0 and time <=24.0:
                        if row[0] == 'r' and row[7] == '2' and row[2] == '2' and row[3] == '5' and row[8] == '4.0' and row[9] == '5.0' and row[4] == "cbr":
                                total_size_24 = total_size_24 + float(8 * float(row[5])/ 10**6)
                                #pcount1 = pcount1 + 14
                                time_field24 = float(row[1])
                                throughput24 = total_size_24/time_field24
                                with open("throughput3e24.txt", "a") as throughput_exp3:
                                        throughput_exp3.write(str(throughput24)+'\n')

		if time >=24.0 and time <=25.0:
                        if row[0] == 'r' and row[7] == '2' and row[2] == '2' and row[3] == '5' and row[8] == '4.0' and row[9] == '5.0' and row[4] == "cbr":
                                total_size_25 = total_size_25 + float(8 * float(row[5])/ 10**6)
                                #pcount1 = pcount1 + 14
                                time_field25 = float(row[1])
                                throughput25 = total_size_25/time_field25
                                with open("throughput3e25.txt", "a") as throughput_exp3:
                                        throughput_exp3.write(str(throughput25)+'\n')












		
	





			
	
 



	'''
        if row[0] == '-' and row[7] == '1' and row[2] == source and row[3] == destination and row[8] == source_addr and row[9] == dest_addr:
                total_size_1 = total_size_1 + float(8 * float(row[5])/ 10**6)
                pcount1 = pcount1 + 1
        time_field1 = float(row[1])
	'''

