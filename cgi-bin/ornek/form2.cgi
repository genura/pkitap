#!/usr/bin/perl
print "Content-type:text/html\n\n";

read(STDIN, $tampon, $ENV{'CONTENT_LENGTH'});
@ciftler = split(/&/, $tampon);
foreach $cift (@ciftler) {
    ($isim, $deger) = split(/=/, $cift);
    $deger =~ tr/+/ /;
    $deger =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;

    $deger =~ s/\n/ /g; # sat�r sonu i�aretlerini yok etmek i�in eklendi

    $FORM{$isim} = $deger;
}

open(DOSYA,">>formbilgileri.txt") or &hata("formbilgileri.txt dosyas� a��lamad�. L�tfen webmaster\@sinanilyas.com adresine mail atarak webmaster'� uyar�n�z.");

print DOSYA "$FORM{'isim'}|$FORM{'email'}|$FORM{'nasilulasti'}|$FORM{'puan'}|";

%secim = ("wds" => "Web Design",
          "wsy" => "Web Server Y�neticili�i",
          "tic" => "Electronic Commerce",
          "als" => "Elektronik Ticaret",
          "egt" => "�nternet Arac�l���yla E�itim" );

foreach $anahtar (keys %secim) {
    if ($FORM{$anahtar} == 1) {
        print DOSYA "$anahtar,";
    }
}

print DOSYA "|$FORM{'yorum'}\n";
close(DOSYA);

print <<HTMLSonu;
<html><head><title>Te�ekk�rler</title></head>
<body>
<h2>Te�ekk�rler</h2>
G�nderdi�iniz bilgiler kaydedildi.
</body></html>
HTMLSonu
;

sub hata {
    ($hatamesaji) = @_;
    print "<h2>Hata!</h2>\n";
    print $hatamesaji;
    exit;
} 