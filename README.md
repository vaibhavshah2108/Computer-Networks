# Computer-Networks
This repository contains five projects that were part of CS5700 curriculum. 

Project-1 : Simple Client
This assignment is intended to familiarize ourselves with writing simple network code. 
Main task is to implement a client program which communicates with a server using sockets. 
The server will ask our client program to solve hundreds of simple mathematical expressions. 
If our program successfully solves all of the expressions, then the server will return a secret flag 
that is unique for each student. To gain extra credit, we need to modify our clients to support SSL connections

For detailed requirements of the project, please visit: http://david.choffnes.com/classes/cs4700sp15/project1.php

Project-2 : Web Crawler
This assignment is intended to familiarize ourselves with the HTTP protocol. 
HTTP is (arguably) the most important application level protocol on the Internet today: the Web runs on HTTP, 
and increasingly other applications use HTTP as well (including Bittorrent, streaming video, Facebook and Twitter's social APIs, etc.).
Main goal in this assignment is to implement a web crawler that gathers data from a fake social networking website that was set up.

High Level Requirement:
Our goal is to collect 5 secret flags that have been hidden somewhere on the Fakebook website. The flags are unique for each student, 
and the pages that contain the flags will be different for each student. Since we have no idea what pages the secret flags will appear on, 
our only option is to write a web crawler that will traverse Fakebook and locate the flags.

For detailed requirements of the project, please visit: http://david.choffnes.com/classes/cs4700sp15/project2.php

Project-3 : Performance Analysis of TCP variants
The objective of this project is to analyze the performance of different(Tahoe, Reno, NewReno,Vegas,SACK) TCP variants. 
We will use the NS-2 network simulator to perform experiments that will help us understand the behavior of the TCP variants under various load conditions and queuing algorithms.

For detailed requirements of the project, please visit: http://david.choffnes.com/classes/cs4700sp15/project3.php

Project-4 : Raw Sockets
The goal of this assignment is to familiarize ourselves with the low-level operations of the Internet protocol stack.
Task is to write a program called rawhttpget that takes one command line parameter (a URL), downloads the associated web page or file, and saves it to the current directory.

For detailed requirements of the project, please visit: http://david.choffnes.com/classes/cs4700sp15/project4.php

Project-5 : Roll your own CDN
In this project, we will create the building blocks of a CDN. First, we will use DNS redirection to send clients to the replica server with the fastest response time.
Second, you will write a simple Web server that returns content requested by clients. Third, you will implement a system that uses information about network performance, load on servers, 
and cached data at servers to determine the best replica server. Performance will be measured in terms of how long it takes to download a piece of content.

For detailed requirements of the project, please visit: http://david.choffnes.com/classes/cs4700sp15/project5.php
