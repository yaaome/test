#!/usr/bin/perl
#	Perl skeleton.plx
#	author: George Tsang
#	Lines that start with pound sign are treated as comments
#	Lines that start with pound sign + exclamation mark combination is known as the "shebang" line
#	The "shebang" line coded in line 1 indicates this Perl file is to be passed to the Perl interpreter residing in subfolder /usr/bin
use strict;
use warnings;
#	The "use" function can be employed to implement pragmas (compiler directives)
#	"use strict" instructs the Perl compiler to check all variables and ensure they are properly declared
#	"use warnings" instructs the Perl compiler to issue all necessary warnings

#	Perl statements and comments

use CGI qw(:standard);

print "Content-type: text/html\n\n";

print "<html><head><title>First</title></head>";
print "<body>";

print "Hello George!\n";

print "</body></html>";
#	Use a semi-colon to terminate each statement. Otherwise, Perl will flag error(s) on the next line.
<>;