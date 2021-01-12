#!/usr/bin/python
# RationalUS.py
# Computes Discharge by Rational Equation  
# Use HMTL POST method
# Use python language
# Computer Name: localhost on Theodore's MacBook Pro 15

# Import modules for CGI handling 
import cgi, cgitb , time

##use warnings;
##use strict;
##use CGI qw( :standard );

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get inputs from fields
runoff_coefficient = float(form.getvalue('runoff_coefficient'))
area = float(form.getvalue('area'))
intensity = float(form.getvalue('intensity'))

# Perform arithmetic
discharge = (1.008)*runoff_coefficient*intensity*area

# Prepare the output HTML 
now = time.strftime("%c")

print "Content-type:text/html\r\n\r\n"  
# should have two returns and line feeds
print "<html>"
print "<head>"
print "<title>Rational Equation Method (US Customary) using Python</title>"
print "</head>"
print "<body>"
print "Discharge by Rational Equation <br/><br/> "
print "Run Date : " , now ," <br/> "
print "------ INPUT VALUES ------ <br/> "
print "        Runoff Coefficient = ", runoff_coefficient," <br/> "
print "        Drainage Area      = ", area , " acres <br/> "
print " Rainfall Intensity        = ", intensity, " inches per hour <br/> "
print "------ COMPUTED DISCHARGE ----- <br/> ";
print "Discharge = ", discharge , " cubic feet per second <br/> "
print "</body>"
print "</html>"

# end of script
