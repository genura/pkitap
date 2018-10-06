#!/usr/bin/perl
$veridosyasi = "ogrenci.txt";
read(STDIN, $tampon, $ENV{'CONTENT_LENGTH'});
@ciftler = split(/&/, $tampon);

foreach $cift (@ciftler) {
   ($alanadi, $deger) = split(/=/, $cift);
   $deger =~ tr/+/ /;
   $deger =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
   $deger =~ s/~!/ ~!/g;
   $FORM{$alanadi} = $deger;
}

$arananmetin = $FORM{'isim'};

open(DOSYA,$veridosyasi);
@bilgiler = <DOSYA>;
close(DOSYA);
print "Content-type:text/html\n\n";
print "<html><head><title>Arama Sonuçlarý</title></head>\n";
print "<body><h3>Arama Sonuçlarý</h3>\n";

$bulunansayisi = 0;

@sonuclar = grep(/$arananmetin/,@bilgiler);

if ($#sonuclar >= 0) {
   foreach $i (@sonuclar) {
       chomp($i);
       ($kayitno,$okulno,$adsoyad,$yas) = split(/\|/,$i);
       print "<b>$adsoyad</b> Okul No: $okulno Yaþ: $yas<br>\n";
       $bulunansayisi++;
   }
print "<br><b>$bulunansayisi</b> kayýt bulundu.<p>\n";
}
else {
   print "Kayýt Bulunamadý.<p>\n";
}

print "</body></html>\n"; 
