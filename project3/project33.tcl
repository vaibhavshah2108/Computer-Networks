#Create a simulator object
set ns [new Simulator]

#Define different colors for data flows (for NAM)
$ns color 1 Blue
$ns color 2 Red

#Open the NAM trace file
set nf [open out1.nam w]
$ns namtrace-all $nf

set tf [open project333.tr w]
$ns trace-all $tf

set bf [open project3aa.tr w]
#Define a 'finish' procedure
proc finish {} {
        global ns nf tf 
        $ns flush-trace
        #Close the NAM trace file
        close $nf
	close $tf
        #Execute NAM on the trace file
        #exec nam out1.nam &
        exit 0
}



#Create four nodes
set 1 [$ns node]
set 2 [$ns node]
set 3 [$ns node]
set 4 [$ns node]
set 5 [$ns node]
set 6 [$ns node]

#Retrieve the command line arguments
set arg1 [lindex $argv 0]      
set arg2 [lindex $argv 1]


#Create links between the nodes
$ns duplex-link $1 $2 10Mb 10ms DropTail
$ns duplex-link $2 $3 10Mb 10ms RED
$ns duplex-link $5 $2 10Mb 10ms DropTail
$ns duplex-link $3 $6 10Mb 10ms DropTail
$ns duplex-link $4 $3 10Mb 10ms DropTail

#Set Queue Size of link (n2-n3) to 10
$ns queue-limit $2 $3 5

#Give node position (for NAM)
$ns duplex-link-op $1 $2 orient right-down
$ns duplex-link-op $5 $2 orient right-up
$ns duplex-link-op $2 $3 orient right
$ns duplex-link-op $4 $3 orient left-down
$ns duplex-link-op $6 $3 orient left-up


#Monitor the queue for link (n2-n3). (for NAM)
#$ns duplex-link-op $n2 $n3 queuePos 0.5


#Setup a TCP connection
set tcp [new Agent/$arg1]
$tcp set class_ 2
$tcp set window_ 15
$ns attach-agent $1 $tcp
set sink [new Agent/TCPSink]
#set sink [new Agent/TCPSink]
$ns attach-agent $4 $sink
$ns connect $tcp $sink
$tcp set fid_ 1

#Setup FTP over TCP
set ftp [new Application/FTP]
$ftp attach-agent $tcp
$ftp set type_ FTP

#Setup a UDP connection
set udp [new Agent/UDP]
$ns attach-agent $5 $udp
set null [new Agent/Null]
$ns attach-agent $6 $null
$ns connect $udp $null
$udp set fid_ 2

#Setup a CBR over UDP connection
set cbr [new Application/Traffic/CBR]
$cbr attach-agent $udp
$cbr set type_ CBR
$cbr set packet_size_ 1000
#set arg2 [lindex $argv 1]
$cbr set rate_ 8mb
$cbr set random_ false

proc record {} {
	global sink null bf
	set ns [Simulator instance]
	set time 0.5
	#puts "Total Bytes = [$null set bytes_]"
	set bandwidth [$sink set bytes_]
	#set bandwidth1 [$null set bytes_]
	#Get the current time
	set now [$ns now]
	#Calculating bandwidth 
	puts $bf "$now [expr $bandwidth/$time*8/1000000]"
	#Reset the bytes_ values on the traffic sink
	$sink set bytes_ 0
	#Reschedule the procedure
	$ns at [expr $now+$time] "record"
}

#Schedule events for the CBR and FTP agents
#$ns at 0.1 "record"
#$ns at 0.1 "$cbr start"
#$ns at 1.0 "$ftp start"
#$ns at 8.5 "$ftp stop"
#$ns at 9.5 "$cbr stop"
if {$arg2 < 11.0} {
	puts "in if"
	#$ns at 0.1 "record"
	$ns at 0.1 "$ftp start"
	$ns at $arg2 "$ftp stop"
} else {
	puts "in else"
	#$ns at 0.1 "record"
	$ns at 0.1 "$ftp start"
	$ns at 10.0 "$cbr start"
	$ns at $arg2 "$ftp stop"
	$ns at $arg2 "$cbr stop"
}	
 
#$ns at 0.1 "$ftp start"
#$ns at 10.0 "$cbr start"
#$ns at 25.0 "$ftp stop"
#$ns at 25.0 "$cbr stop"
#Detach tcp and sink agents (not really necessary)
#$ns at 4.5 "$ns detach-agent $n0 $tcp ; $ns detach-agent $n3 $sink"

#Call the finish procedure after 5 seconds of simulation time
$ns at $arg2 "finish"


#Print CBR packet size and interval
puts "CBR packet size = [$cbr set packet_size_]"
puts "CBR interval = [$cbr set interval_]"
#puts "Bytes received at TCP Sink = [$bytes_received set bytes_]"
#Run the simulation
$ns run
