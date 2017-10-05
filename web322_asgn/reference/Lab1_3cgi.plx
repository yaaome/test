#!/usr/bin/perl
#  Lab1_3cgi.plx
use CGI qw( :standard );

my $name = param( "name" );
my $password = param( "password" );

print "Content-type: text/html\n\n";
print "<!DOCTYPE html>";
print "<html>";
print "<head>";
print "<meta charset=\"UTF-8\" />";
print "<title>First CGI Program</title>";
print "</head>";
print "<body>";
print "<h1 style='color: #00f;'>Hello ";
print $name;
print "!";
print "<br />Your password is ";
print $password;
print ".</h1>";
print "</body>";
print "</html>";
