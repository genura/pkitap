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

# "Bu siteye nas�l ula�t�n�z?" sorusunun cevab�
# numara olarak g�nderildi�i i�in bunu �evirebilmek
# i�in bir hash de�i�kene ihtiyac�m�z var

%nasilulasti = ( 0 => "",
                 1 => "Direk adresini yazd�m",
                 2 => "Siteyi bookmark etmi�tim",
                 3 => "Arama motorundan buldum",
                 4 => "Ba�ka bir siteden",
                 5 => "Adresi bir kitaptan ald�m",
                 6 => "Di�er" );

print <<HTMLBas;
<html><head><title>Sonu�lar</title></head>
<body>
<h2>Sonu�lar</h2>

Formla g�nderdi�iniz bilgiler a�a��daki �ekildedir:<p>

�sminiz: $FORM{'isim'}<p>

E-mail adresiniz: $FORM{'email'}<p>

Siteye nas�l ula�t���n�z: $nasilulasti{$FORM{'nasilulasti'}}<p>

Siteye verdi�iniz puan: $FORM{'puan'}<p>

HTMLBas
;

%secim = ("wds" => "Web Design",
          "wsy" => "Web Server Y�neticili�i",
          "tic" => "Elektronik Ticaret",
          "als" => "�nternetten Al��veri�",
          "egt" => "�nternet Arac�l���yla E�itim" );

print "A�a��daki konularla ilgileniyorsunuz:<br>\n";
foreach $anahtar (keys %secim) {
   if ($FORM{$anahtar} == 1) {
      print "$secim{$anahtar}<br>\n";
   }
}

print <<HTMLSon;
<p>
Sayfa hakk�nda yorumlar�n�z:<br>
$FORM{'yorum'}
<p>
</body></html>
HTMLSon
; 