#!/usr/bin/perl

print "Content-type:text/html\n\n";

read(STDIN, $tampon, $ENV{'CONTENT_LENGTH'});
@ciftler = split(/&/, $tampon);
foreach $cift (@ciftler) {
   ($isim, $deger) = split(/=/, $cift);
   $deger =~ tr/+/ /;
   $deger =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
   $FORM{$isim} = $deger;
}

print "<html><head><title>Form Bilgileri</title></head><body>";
print "<h2>Formla gönderilen bilgiler:</h2>\n";

foreach $anahtar (keys(%FORM)) {
   print "$anahtar = $FORM{$anahtar}<br>";
}

print "</body></html>"; 
