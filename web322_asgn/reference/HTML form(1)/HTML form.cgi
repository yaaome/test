#!/usr/bin/perl
#	HTML form.cgi
#	author: George Tsang
#	http://zenit.senecac.on.ca/~george.tsang/cgi-bin/HTML%20form.cgi

use strict;
use warnings;
use CGI qw(:standard);																#	import functions from CGI.pm

my $input = param ("txtInput");

#	Webpage starts ==========

my $html_head = <<EHTMLHEAD;
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8" />
	<title>&lt;form&gt;</title>
</head>

EHTMLHEAD

my $html_body = <<EHTMLBODY;
<body>

	<h1>&lt;form&gt;</h1>
	
	<form method="post" action="HTML form.cgi">

		<input name="txtInput" type="text" />
						
		<br />
		<br />
		<button type="submit" value="Submit">Submit</button>
						
		<br />
		<br />

EHTMLBODY

print "Content-type: text/html\n\n";
print $html_head."\n";

#	print '$rdoDHockney = '.$rdoDHockney;

if ($input)																	#	Check if this CGI was invoked with parameters
{
		print $html_body."\n";

		print"\t\t<label>You have entered ".$input.".</label>";
}
else
{
		print $html_body."\n";

		print"\t\t<label>You have entered nothing.</label>";
}

print "\n\t</form>\n</body>\n"."</html>\n";

#	Webpage ends ==========
