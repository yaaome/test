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
	<script src="https://code.jquery.com/jquery-1.10.2.js"></script>
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
				<input id="macintoshclassic" type="radio" name="model" value="macintoshclassic"> macintoshclassic <br>
				<input id="msx" type="radio" name="model" value="msx"> msx <br>
				<input id="tandy_trs80" type="radio" name="model" value="tandy_trs80"> tandy_trs80 <br>
				
				<br>
				<input type="submit" value="submit">
			</form> 
		</div>
	
		<div id="img_container">
			<img src="../images/atari.jpg" alt="NO IMAGE" id="im">
		</div>
		

	<script> $(document).ready(function(){
			$("#sending").submit(function( event ) {
			$("#im").attr("src", "images/ipad.jpg");
			});
});
 </script>
	</main>
	
		<footer>
			Name: Jin Lee<br>
			Student Number: 123456789
		</footer>
	</main>

EHTMLBODY

print "Content-type: text/html\n\n";
print $html_head."\n\n";


if ($input == "atari")																	#	Check if this CGI was invoked with parameters
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