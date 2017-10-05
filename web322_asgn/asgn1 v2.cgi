#!/usr/bin/perl
#	asgn1.cgi
#	author: Jin Lee
#	http://zenit.senecac.on.ca/~int322_173sa11/cgi-bin/asgn1.cgi

use strict;
use warnings;
use CGI qw(:standard);																#	import functions from CGI.pm


my $input = param ("model");
if ($input eq "")
{
	$input = "history";
}
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
			<form id="sending" action="http://zenit.senecac.on.ca/~int322_173sa11/cgi-bin/asgn1 v2.cgi">
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

sub imgsrc {
	my ($imgname) = @_;
  ##  print "$_[0]. <p> value </p>"; 
	print '<div id="img_container">
			<img src="../images/'.$_[0].'.jpg" alt="NO IMAGE" id="im">
			<div id="p_desc">
				<p>'.$_[0].'</p>
			</div>
		</div>
	</main> ';
}
	

print "Content-type: text/html\n\n";
print $html_head."\n\n";


if ($input eq "atari")																	
{
		print $html_body."\n";
		imgsrc($input);
}

elsif ($input eq "ipad")																	
{
		print $html_body."\n";
		imgsrc($input);
}

elsif ($input eq "galaxys8")																	
{
		print $html_body."\n";
		imgsrc($input);
}

elsif ($input eq "macintosh_classic")																	
{
		print $html_body."\n";
		imgsrc($input);
}

elsif ($input eq "msx")																	
{
		print $html_body."\n";
		imgsrc($input);
}

elsif ($input eq "tandy_trs80")																	
{
		print $html_body."\n";
		imgsrc($input);
}
else
{
		print $html_body."\n";
		imgsrc($input);
}
	

print $html_footer;
print "</body>\n"."</html>\n";

#	Webpage ends ==========