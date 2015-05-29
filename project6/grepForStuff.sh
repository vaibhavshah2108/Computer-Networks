#!/bin/bash

filename="/home/hegde.vi/pcap-decrypted/2015-Apr-24/*"

#filename="$1"
for eachtrace in $filename;
do
	

	tcpdump -Ar $eachtrace| grep -v 'TCP' | grep -v 'HTTP' | grep -v 'seq' > httpdata2.txt
	echo $eachtrace

	echo "-Looking for lat=, latitude="
	egrep -io "[^a-zA-Z]?lat([^a-zA-Z]|itude).*[0-9]+(\.?)[0-9]+" httpdata2.txt | sort | uniq -c

#echo " Looking for pw=, pwd=, password=, user= " #generalized password and username. commented out because we searched for phone-specific
#egrep -io "[^a-zA-Z]?pw[^a-zA-Z]?([=:])+(\"?)....." httpdata.txt | sort | uniq -c
#egrep -io "[^a-zA-Z]?pwd[^a-zA-Z]?([:=])+(\"?)...." httpdata.txt | sort | uniq -c
#egrep -io "[^a-zA-Z]?password[^a-zA-Z]?([:=])+(\"?)...." httpdata.txt | sort | uniq -c
#egrep -io "[^a-zA-Z]?user[^a-zA-Z]?([:=])+(\"?)...." httpdata.txt | sort | uniq -c

#echo " Looking for IMEI=  " #generalized imei. commented out because we searched for phone specific.
#egrep -io "[^a-zA-Z]?IMEI[^a-zA-Z]?([:=])+(\"?)[0-9]{15,}" httpdata.txt | sort | uniq -c
#egrep -io "[^a-zA-Z]?udid[^a-zA-Z]?([:=])+(\"?)[0-9]{15,}" httpdata.txt | sort | uniq -c
#egrep -io "[^a-zA-Z]?uuid[^a-zA-Z]?([:=])+(\"?)[0-9]{15,}" httpdata.txt | sort | uniq -c
#egrep -io "[^a-zA-Z]?-Id[^a-zA-Z]?([:=])+(\"?)[0-9]{15,}" httpdata.txt | sort | uniq -c

	echo "Looking for phone specific things"
	#phone-specific searches
	#grep -i "353216057521895" httpdata.txt | sort | uniq -c
	grep -i "355031040753366" httpdata2.txt | sort | uniq -c
	#grep -i "[355031040753366]" httpdata.txt | sort | uniq -c
	grep -i "XT1058" httpdata2.txt | sort | uniq -c
	grep -i "vinayhegde2010@gmail.com" httpdata2.txt | sort | uniq -c
	grep -i "hegde.vi" httpdata2.txt | sort | uniq -c
	grep -i "hegde5" httpdata2.txt | sort | uniq -c
	grep -i "hegde.vi@husky.neu.edu" httpdata2.txt | sort | uniq -c
	grep -i "Vinay" httpdata2.txt | sort| uniq -c
	#grep -i "amobee.com" httpdata.txt | sort | uniq -c
	grep -i "ghost" httpdata2.txt | sort | uniq -c
	#grep -i "617373" httpdata.txt | sort | uniq -c
	grep -i "36304FED50047E3C" httpdata2.txt | sort | uniq -c
	grep -i "tonikroos" httpdata2.txt | sort | uniq -c
	grep -i "vanpersie" httpdata2.txt | sort | uniq -c
	grep -i "Roxbury" httpdata2.txt | sort | uniq -c	
	grep -i "macAddress=" httpdata2.txt | sort | uniq -c
	grep -i "42.3600825" httpdata2.txt | sort | uniq -c
	grep -i "vinay" httpdata2.txt | sort | uniq -c
	grep -i "govindarajulu" httpdata2.txt | sort | uniq -c
	grep -i "vanny" httpdata2.txt | sort | uniq -c
	grep -i "stretfordend" httpdata2.txt | sort | uniq -c
	grep -i "vinayhegde1993@gmail.com" httpdata2.txt | sort | uniq -c
	grep -i "corine" httpdata2.txt | sort | uniq -c
	grep -i "f8:f1:b6:4e:8d:6f" httpdata2.txt | sort | uniq -c
	#grep -i ".edu" httpdata.txt | sort | uniq -c
	#grep lat
	#grep -i "" httpdata.txt | sort | uniq -c

	#contact info (phone specific)
	grep -i "Dhanush" httpdata2.txt | sort | uniq -c
	grep -i "16173730582" httpdata2.txt | sort | uniq -c
	grep -i "1-617-373-0581" httpdata2.txt | sort | uniq -c
	grep -i "1-617-373-0580" httpdata2.txt | sort | uniq -c
	grep -i "+919900419415" httpdata2.txt | sort | uniq -c

	echo " Looking for phone number, also phone=, number=  "	
	egrep -io "[^a-zA-Z]?number[^a-zA-Z]?([:=])+(\"?).........." httpdata2.txt | sort | uniq -c
	egrep -io "[^a-zA-Z]?phone[^a-zA-Z]?([:=])+(\"?)........." httpdata2.txt | sort | uniq -c

	echo " Looking for credit card numbers "
	egrep -io '4[0-9]{12}(?:[0-9]{3})?' httpdata2.txt | sort  | uniq -c #Visa
	egrep -io '5[1-5][0-9]{14}' httpdata2.txt | sort | uniq -c #MasterCard
	egrep -io '[47][0-9]{13}' httpdata2.txt | sort | uniq -c #AmEx
	egrep -io '3(?:0[0-5]|[68][0-9])[0-9]{11}' httpdata2.txt | sort | uniq -c #DinersClub
	egrep -io '6(?:011|5[0-9]{2})[0-9]{12}' httpdata2.txt | sort | uniq -c #Discover
	egrep -io '(?:2131|1800|35\d{3})\d{11}' httpdata2.txt | sort | uniq -c #JCB

	echo "\nLooking for email addresses"
	echo $(egrep -io "[^ ]+@([a-z]+\.)+(((com)|(org))|((edu)|(net)))" httpdata2.txt)

done

