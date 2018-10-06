#!/usr/bin/perl

%sayfalar = ("sinan" => "http://www.sinanilyas.com",
             "koray" => "http://cc.sau.edu.tr/~ktoksoz",
             "baris" => "http://turk.eu.org/uruzgar" );

print "Content-type:text/html\n\n";

print <<IlkKisim;
<html><head><title>Adres Listesi</title></head>
<body>
<h2>Adres Listesi</h2>
<ul>
IlkKisim
;

foreach $anahtar (keys %sayfalar) {
print "<li><a href=\"$sayfalar{$anahtar}\">$anahtar</a>\n"; 
}

print <<SonKisim;
</ul>
<p>
</body>
</html>
SonKisim
; 