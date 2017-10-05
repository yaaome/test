#!/usr/bin/perl
#	asgn1.cgi
#	author: Jin Lee
#	http://zenit.senecac.on.ca/~int322_173sa11/cgi-bin/asgn1.cgi

use strict;
use warnings;
use CGI qw(:standard);																#	import functions from CGI.pm

my $input = param ("model");

#	Webpage starts ==========

my $html_head = <<EHTMLHEAD;
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8" />
	<title>WEB322 Assignment 1</title>
	<link rel="stylesheet" href="../css/asgn1.css">
</head>

EHTMLHEAD

my $html_body = <<EHTMLBODY;
<body>

	<header>
		WEB 322 Assignment 1
	</header>

	<main>
			
 
		<div id="rbtn_container">
			<form id="sending" action="http://zenit.senecac.on.ca/~int322_173sa11/cgi-bin/asgn1.cgi">
				<input id="atari" type="radio" name="model" value="atari"> atari <br>
				<input id="galaxys8" type="radio" name="model" value="galaxys8"> galaxys8 <br>
				<input id="ipad" type="radio" name="model" value="ipad"> ipad <br>
				<input id="macintosh_classic" type="radio" name="model" value="macintosh_classic"> macintosh classic <br>
				<input id="msx" type="radio" name="model" value="msx"> msx <br>
				<input id="tandy_trs80" type="radio" name="model" value="tandy_trs80"> tandy_trs80 <br>
				<br>
				<input type="submit" value="submit">
			</form> 
		</div>
	
EHTMLBODY

my $html_footer = <<EHTMLFOOTER;
	
		<footer>
			Name: Jin Lee<br>
			Student Number: 123456789
		</footer>
	</main>
	
EHTMLFOOTER

print "Content-type: text/html\n\n";
print $html_head."\n\n";


if ($input eq "atari")																	
{
		print $html_body."\n";
		print '<div id="img_container">
			<img src="../images/atari.jpg" alt="NO IMAGE" id="im">
		</div>
	</main> ';
}

elsif ($input eq "ipad")																	
{
		print $html_body."\n";

		print '<div id="img_container">
			<img src="../images/ipad.jpg" alt="NO IMAGE" id="im">
		</div>
	</main> ';
}

elsif ($input eq "galaxys8")																	
{
		print $html_body."\n";

		print '<div id="img_container">
			<img src="../images/'.$input.'.jpg" alt="NO IMAGE" id="im">
		</div>
	</main> ';
}

elsif ($input eq "macintosh_classic")																	
{
		print $html_body."\n";

		print '<div id="img_container">
			<img src="../images/macintosh_classic.jpg" alt="NO IMAGE" id="im">
		</div>
	</main> ';
}

elsif ($input eq "msx")																	
{
		print $html_body."\n";

		print '<div id="img_container">
			<img src="../images/msx.jpg" alt="NO IMAGE" id="im">
		</div>
	</main> ';
}

elsif ($input eq "tandy_trs80")																	
{
		print $html_body."\n";

		print '<div id="img_container">
			<img src="../images/tandy_trs80.jpg" alt="NO IMAGE" id="im">
		</div>
	</main> ';
}
else
{
		print $html_body."\n";

		print '<div id="img_container">
			<img src="../images/default_img.jpg" alt="NO IMAGE" id="im">
		</div>
	</main> ';
}
	

print $html_footer;
print "</body>\n"."</html>\n";

#	Webpage ends ==========