#!/usr/bin/perl

print "Content-type:text/html\n\n";
print <<HTMLSonu;
<html><head><title>Ortam De�i�kenleri</title></head>
<body>
HTMLSonu
;

foreach $anahtar (sort(keys %ENV)) {
   print "$anahtar = $ENV{$anahtar}<br>\n";
}

print "</body></html>";
