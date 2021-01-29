# ENGR-1330 Computational Thinking and Data Science
This is a repository for a course at Texas Tech University, specificially the sections taught by Dr. Theodore G. Cleveland.

## Purpose
The purpose of the repository is to maintain a convienent back-up of course content for rapid migration across servers.  

## Special Notes
1. The structure is written to work on a web host, with hostname == `atomickitty.ddns.net`, if you clone to another server you will have the lovely task of changing the links.  The string editor `sed` will become your friend!

2. Materials herein come from many sources, in particular the Data8 repository from UC Berkeley.  Sources in notebooks are at least cited by a URL.  As the content is matured, proper citations are to be inserted.

3. The `3-Readings` directory contains copyrighted materials an should be exposed with care on a web server; generally no-one reads anymore, so its probably safe enought to protect using `.htaccess` simple uid:pwd approach. I use the materials during lectures to point out where I obtain various computational ideas.

## How to Use
1. Clone the entire repository to /var/www/html/engr-1330-webroot.  Have your main index point to this directory i.e. `http://your-fqdn-server.org/engr-1330-webroot/`
You can see working example at http://atomickitty.ddns.net/compthink/ (I use a symlink to the engr-1330-webroot)


