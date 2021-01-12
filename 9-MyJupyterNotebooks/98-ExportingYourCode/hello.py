#!/usr/bin/python   
# above line is part of a cgi-bin script -- do not omit it!
import cgitb  # debugging shit, ok to omit
cgitb.enable() # debugging shit, ok to omit
print ('Content-type:text/html\r\n\r\n')
print('<html>')
print('<head><title>Hello from Python via CGI-BIN</title></head>')
print('<body>')
print('Hello from python via cgi-bin, runs on localhost')
print('</body>')
print('</html>')