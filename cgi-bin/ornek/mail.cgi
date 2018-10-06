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

$mailprog = '/usr/sbin/sendmail';

# bunu kendi mail adresinizle de�i�tirin

$gonderilen = 'sinan@sinanilyas.com';

# burada maili g�ndermek �zere sendmail program� a��l�yor
# e�er sendmail program� bulunamazsa hata alt program� (en altta)
# i�letilerek program�n bulunamad��� yaz�yor

open (MAIL, "|$mailprog -t") or &hata("$mailprog bulunamad�!\n");

# sendmail program�na mailin kime g�nderilece�i bildiriliyor

print MAIL "To: $gonderilen\n";

# sendmail program�na ziyaret�inin email adresi bildiriliyor.
# bu "Yan�tla" tu�una bast���n�zda i�e yarar
# kullanmak zorunda de�ilsiniz
# formunuzda 'email' ve 'isim' kutular�n�n bulundu�u varsay�lm��t�r.

print MAIL "Reply-to: $FORM{'email'}\n";

# sendmail program�na mailin konusu g�nderiliyor
# konudan sonra iki tane \n oldu�una dikkat edin

print MAIL "Subject: Form Bilgileri\n\n";

# sendmail program�na form bilgileri g�nderiliyor

foreach $anahtar (keys(%FORM)) {
   print MAIL "$anahtar = $FORM{$anahtar}\n";
}

# bilgiler g�nderildikten sonra sendmail program�n� kapatmay� unutmay�n

close(MAIL);

# te�ekk�r sayfas� olu�turuluyor

print <<HTMLSonu;
<html><head><title>Te�ekk�rler</title></head><body>
<h2>Te�ekk�rler</h2>
Mailiniz g�nderildi. Formu g�nderdi�iniz i�in te�ekk�rler<p>
</body></html>
HTMLSonu
;

# hata alt program�

sub hata {
    ($hatamesaji) = @_;
    print "<html><head><title>Hata!</title></head><body>";
    print "<h2>Hata</h2>\n";
    print "$hatamesaji<p>\n";
    print "</body></html>\n";
    exit;
}
