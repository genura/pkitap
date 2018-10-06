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

print "<html><head><title>Sonuçlar</title></head>\n";
print "<body>\n";
print "<h2>Sonuçlar</h2>\n";

@renkler = ("kirmizi","sari","yesil","mavi");
foreach $renk (@renkler) {
    if ($FORM{$renk} == 1) {
       print "$renk rengini iþaretlediniz<br>\n";
    }
}

print "</body></html>\n"; 