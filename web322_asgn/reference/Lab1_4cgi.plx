#!/usr/bin/perl
#  Lab1_4cgi.plx
use CGI qw( :standard );
print redirect ("http://zenit.senecac.on.ca/~george.tsang/Lab1_3.htm");

print "Content-type: text/html\n\n";

print "<!DOCTYPE html>";
print "<html>";
print "<head>";
print "<meta charset=\"UTF-8\" />";
print "<title>Redirecting CGI Program</title>";
print "</head>";
print "<body>";

$a = "";
$b = "0";
$c = 0;

if($a){
print "a is true<br>";
}else{
print "a is false<br>";
}

if($b){
print "b is true<br>";
}else{
print "b is false<br>";
}

if($c){
print "c is true<br>";
}else{
print "c is false<br>";
}

if($d){
print "d is true<br>";
}else{
print "d is false<br>";
}

print "</body>";
print "</html>";
