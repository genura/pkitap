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

# "Bu siteye nasýl ulaþtýnýz?" sorusunun cevabý
# numara olarak gönderildiði için bunu çevirebilmek
# için bir hash deðiþkene ihtiyacýmýz var

%nasilulasti = ( 0 => "",
                 1 => "Direk adresini yazdým",
                 2 => "Siteyi bookmark etmiþtim",
                 3 => "Arama motorundan buldum",
                 4 => "Baþka bir siteden",
                 5 => "Adresi bir kitaptan aldým",
                 6 => "Diðer" );

print <<HTMLBas;
<html><head><title>Sonuçlar</title></head>
<body>
<h2>Sonuçlar</h2>

Formla gönderdiðiniz bilgiler aþaðýdaki þekildedir:<p>

Ýsminiz: $FORM{'isim'}<p>

E-mail adresiniz: $FORM{'email'}<p>

Siteye nasýl ulaþtýðýnýz: $nasilulasti{$FORM{'nasilulasti'}}<p>

Siteye verdiðiniz puan: $FORM{'puan'}<p>

HTMLBas
;

%secim = ("wds" => "Web Design",
          "wsy" => "Web Server Yöneticiliði",
          "tic" => "Elektronik Ticaret",
          "als" => "Ýnternetten Alýþveriþ",
          "egt" => "Ýnternet Aracýlýðýyla Eðitim" );

print "Aþaðýdaki konularla ilgileniyorsunuz:<br>\n";
foreach $anahtar (keys %secim) {
   if ($FORM{$anahtar} == 1) {
      print "$secim{$anahtar}<br>\n";
   }
}

print <<HTMLSon;
<p>
Sayfa hakkýnda yorumlarýnýz:<br>
$FORM{'yorum'}
<p>
</body></html>
HTMLSon
; 