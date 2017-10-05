#!/usr/bin/perl
#	Perl CGI Generate HTML.plx
#	author: George Tsang
#	http://zenit.senecac.on.ca/~george.tsang/cgi-bin/examples/blackboard/cgi/Perl CGI Generate HTML.plx

use strict;
use warnings;
use CGI qw(:standard);																#	import functions from CGI.pm

print "Content-type: text/html\n\n";

print "<!DOCTYPE html>\n<html>\n<head>\n\t<meta charset='UTF-8' />\n\t<title>Perl CGI Generate HTML</title>\n</head>\n<body style='text-align: center;'>\n\t<p style='color: red;'>Hello world! Your clock is now ".scalar(localtime())."</p>\n</body>\n</html>\n";

