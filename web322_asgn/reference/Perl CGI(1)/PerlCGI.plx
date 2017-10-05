#!/usr/bin/perl
#	PerlCGI.plx
#	author: George Tsang

#	The %ENV hash is a built-in hashtable in Perl that contains the names and values of all the environment variables.
#	The names of the environment variables are the keys used to access the associated values of the environment variables.
#	Input from webpages to CGI can be submitted via various methods.
#	1. When using the GET method, the environment variable QUERY_STRING is populated by form information that is appended to the URL 
#	following a question mark (?) that serves as a delimiter.
#	2. When using the POST method, the environment variable CONTENT_LENGTH is set to the total number of characters submitted by the webpage.
#	The submitted information is to be inputted via STDIN.

use strict;
use warnings;
use Data::Dumper;
use CGI qw(:standard);																#	import functions from CGI.pm

our $FirstName;
our $LastName;
our $chkAppliances;
our $rdoAutomobiles;
our $selPerformance;

our $i;
our $key;

print "Content-type: text/html\n\n";
print "<pre>\n";

$FirstName = param ("FirstName");
$LastName = param ("LastName");
$chkAppliances = param ("chkAppliances");
$rdoAutomobiles = param ("rdoAutomobiles");
$selPerformance = param ("selPerformance");

print "********** Values submitted from the browser that are individually extracted by the param function\n\n";
print "\$FirstName = $FirstName\n";
print "\$LastName = $LastName\n";
print "\$chkAppliances = $chkAppliances\n";
print "\$rdoAutomobiles = $rdoAutomobiles\n";
print "\$selPerformance = $selPerformance\n\n";

print "********** Values submitted from the browser that are extracted by param function using for loop\n\n";
for $i (param()) {
    print "<b>$i</b>: ", param($i), "<br />";
}

print "\n********** Environment variables from the \%ENV hashtable\n\n";
foreach $key (sort keys(%ENV)) {
  print "$key = $ENV{$key}<br />";
}
print "</pre>\n";
