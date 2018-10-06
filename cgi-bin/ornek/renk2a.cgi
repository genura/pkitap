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

%renkler = ("kirmizi" => "red",
            "sari" => "yellow",
            "yesil" => "green",
            "mavi" => "blue");
print "<html><head><title>En Sevdiðiniz Renk</title></head>\n";
print "<body bgcolor=$renkler{$FORM{'renk'}}>\n";
print "<h2>En sevdiðiniz renk: $FORM{'renk'}</h2><br>\n";
print "</body></html>"; 