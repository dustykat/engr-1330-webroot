# ENGR-1330 Computational Thinking and Data Science
This is a repository for a course at Texas Tech University, specificially the sections taught by Dr. Theodore G. Cleveland.

## Purpose
The purpose of the repository is to maintain a convienent back-up of course content for rapid migration across servers.  

## Special Notes
1. The structure is written to work on a web host, with hostname == `54.243.252.9`, if you clone to another server you will have the lovely task of changing the links.  The string editor `sed` will become your friend!

2. Materials herein come from many sources, in particular the Data8 repository from UC Berkeley.  Sources in notebooks are at least cited by a URL.  As the content is matured, proper citations are to be inserted.

3. The `3-Readings` directory contains copyrighted materials and should be exposed with care on a web server; generally no-one reads anymore, so its probably safe enought to protect using `.htaccess` simple uid:pwd approach. I use the materials during lectures to point out where I obtain various computational ideas.

## Ways to Use
1. Clone the entire repository directly to /var/www/html/engr-1330-webroot.  
2. Clone the repository to somewhere else, then as root make a symbolic link to the location like ```ln -s /home/myshit/engr-1331-webroot /var/www/html/engr-1331-webroot```  You can see working example at https://54.243.252.9/engr-1330-webroot/ (You will have to set a browser exception to accept the self-signed certificate)
3. Clone to your local machine, and extract what you need.


## Syncronization Notes:
1. Sync with 54.243.252.9/engr-1330-webroot/ (AWS server -- primary and live website copy)
2. Sync with 75.3.84.227:192.168.1.75/ (Raspberry Pi -- developer and backup website copy)

