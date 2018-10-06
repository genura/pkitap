#!/usr/bin/perl
print "Content-type:text/html\n\n";

open(DOSYA,"formbilgileri.txt") or &hata("formbilgileri.txt dosyas� a��lamad�. L�tfen webmaster\@sinanilyas.com adresine mail atarak webmaster'a haber verin.");

@bilgiler = <DOSYA>;
close(DOSYA);

# Bilgileri �zetlemek i�in �nce baz� de�i�kenler haz�rlan�yor.
$sayi = 0; # Formu g�nderenlerin say�s�
$toplampuan = 0; # Verilen puanlar�n toplam�
$yorumlar = ""; # G�nderilen b�t�n yorumlar
%nasilulasti_sayisi = (); # Hangi �ekilde ka� ki�inin ula�t���
%ilgi = (); # Hangi bilgisayar alan�yla ka� ki�inin ilgilendi�inin say�s�

%nasilulasti = ( 0 => "",
                 1 => "Direk adresini yazd�m",
                 2 => "Siteyi bookmark etmi�tim",
                 3 => "Arama motorundan buldum",
                 4 => "Ba�ka bir siteden",
                 5 => "Adresi bir kitaptan ald�m",
                 6 => "Di�er" );

foreach $i (@bilgiler) {
chomp($i);
($isim,$email,$nasil,$puan,$secim,$yorum) = split(/\|/,$i);

   # Bu sat�r "$sayi = $sayi + 1" ile ayn� i�i g�r�r.
   $sayi++;

   $toplampuan = $toplampuan + $puan;

   # Bu sat�r $yorumlar de�i�keninin sonuna $yorum de�i�keninin
   # i�eri�ini ekler. 

   $yorumlar .= "$yorum\n"; 

   $nasilulasti_sayisi{$nasil}++;

   @ilgilistesi = split(/,/,$secim);
   foreach $j (@ilgilistesi) {
      $ilgi{$j}++;
   }
}

# Verilen puanlar�nn ortalamas� bulunuyor.

if ($sayi > 0) { # S�f�ra b�lmemek i�in
   $ort_puan = int($toplampuan / $sayi);
} else {
   $ort_puan = 0;
}

# Sonu�lar� bildiren web sayfas� haz�rlan�yor.

print <<HTMLSonu;
<html><head><title>�zet</title></head>
<body>
<h2>�zet</h2>

G�nderilen form say�s�: $sayi<p>

Verilen puanlar�n ortalamas�: $ort_puan<p>

Siteye ka� ki�inin ne �ekilde ula�t���:<br>
<ul>
   <li>(yan�tlamayan) - $nasilulasti_sayisi{0}
   <li>$nasilulasti{1} - $nasilulasti_sayisi{1}
   <li>$nasilulasti{2} - $nasilulasti_sayisi{2}
   <li>$nasilulasti{3} - $nasilulasti_sayisi{3}
   <li>$nasilulasti{4} - $nasilulasti_sayisi{4}
   <li>$nasilulasti{5} - $nasilulasti_sayisi{5}
   <li>$nasilulasti{6} - $nasilulasti_sayisi{6}
</ul>

Ka� ki�inin hangi bilgisayar alan�yla ilgili oldu�u:<br>
<ul>
   <li>Web Design: $ilgi{'wds'}
   <li>Web Server Y�neticili�i: $ilgi{'wsy'}
   <li>Electronic Commerce: $ilgi{'tic'}
   <li>Elektronik Ticaret: $ilgi{'tic'}
   <li>�nternet Arac�l���yla E�itim: $ilgi{'egt'}
</ul><p>

Sayfa Hakk�nda Yorumlar:<p>
$yorumlar

HTMLSonu
;

sub hata {
   ($hatamesaji) = @_;
   print "<h2>Hata!</h2>\n";
   print $hatamesaji;
   exit;
}
