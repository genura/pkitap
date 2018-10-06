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

# bunu kendi mail adresinizle deðiþtirin

$gonderilen = 'sinan@sinanilyas.com';

# burada maili göndermek üzere sendmail programý açýlýyor
# eðer sendmail programý bulunamazsa hata alt programý (en altta)
# iþletilerek programýn bulunamadýðý yazýyor

open (MAIL, "|$mailprog -t") or &hata("$mailprog bulunamadý!\n");

# sendmail programýna mailin kime gönderileceði bildiriliyor

print MAIL "To: $gonderilen\n";

# sendmail programýna ziyaretçinin email adresi bildiriliyor.
# bu "Yanýtla" tuþuna bastýðýnýzda iþe yarar
# kullanmak zorunda deðilsiniz
# formunuzda 'email' ve 'isim' kutularýnýn bulunduðu varsayýlmýþtýr.

print MAIL "Reply-to: $FORM{'email'}\n";

# sendmail programýna mailin konusu gönderiliyor
# konudan sonra iki tane \n olduðuna dikkat edin

print MAIL "Subject: Form Bilgileri\n\n";

# sendmail programýna form bilgileri gönderiliyor

foreach $anahtar (keys(%FORM)) {
   print MAIL "$anahtar = $FORM{$anahtar}\n";
}

# bilgiler gönderildikten sonra sendmail programýný kapatmayý unutmayýn

close(MAIL);

# teþekkür sayfasý oluþturuluyor

print <<HTMLSonu;
<html><head><title>Teþekkürler</title></head><body>
<h2>Teþekkürler</h2>
Mailiniz gönderildi. Formu gönderdiðiniz için teþekkürler<p>
</body></html>
HTMLSonu
;

# hata alt programý

sub hata {
    ($hatamesaji) = @_;
    print "<html><head><title>Hata!</title></head><body>";
    print "<h2>Hata</h2>\n";
    print "$hatamesaji<p>\n";
    print "</body></html>\n";
    exit;
}
