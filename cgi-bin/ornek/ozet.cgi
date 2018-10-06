#!/usr/bin/perl
print "Content-type:text/html\n\n";

open(DOSYA,"formbilgileri.txt") or &hata("formbilgileri.txt dosyasý açýlamadý. Lütfen webmaster\@sinanilyas.com adresine mail atarak webmaster'a haber verin.");

@bilgiler = <DOSYA>;
close(DOSYA);

# Bilgileri özetlemek için önce bazý deðiþkenler hazýrlanýyor.
$sayi = 0; # Formu gönderenlerin sayýsý
$toplampuan = 0; # Verilen puanlarýn toplamý
$yorumlar = ""; # Gönderilen bütün yorumlar
%nasilulasti_sayisi = (); # Hangi þekilde kaç kiþinin ulaþtýðý
%ilgi = (); # Hangi bilgisayar alanýyla kaç kiþinin ilgilendiðinin sayýsý

%nasilulasti = ( 0 => "",
                 1 => "Direk adresini yazdým",
                 2 => "Siteyi bookmark etmiþtim",
                 3 => "Arama motorundan buldum",
                 4 => "Baþka bir siteden",
                 5 => "Adresi bir kitaptan aldým",
                 6 => "Diðer" );

foreach $i (@bilgiler) {
chomp($i);
($isim,$email,$nasil,$puan,$secim,$yorum) = split(/\|/,$i);

   # Bu satýr "$sayi = $sayi + 1" ile ayný iþi görür.
   $sayi++;

   $toplampuan = $toplampuan + $puan;

   # Bu satýr $yorumlar deðiþkeninin sonuna $yorum deðiþkeninin
   # içeriðini ekler. 

   $yorumlar .= "$yorum\n"; 

   $nasilulasti_sayisi{$nasil}++;

   @ilgilistesi = split(/,/,$secim);
   foreach $j (@ilgilistesi) {
      $ilgi{$j}++;
   }
}

# Verilen puanlarýnn ortalamasý bulunuyor.

if ($sayi > 0) { # Sýfýra bölmemek için
   $ort_puan = int($toplampuan / $sayi);
} else {
   $ort_puan = 0;
}

# Sonuçlarý bildiren web sayfasý hazýrlanýyor.

print <<HTMLSonu;
<html><head><title>Özet</title></head>
<body>
<h2>Özet</h2>

Gönderilen form sayýsý: $sayi<p>

Verilen puanlarýn ortalamasý: $ort_puan<p>

Siteye kaç kiþinin ne þekilde ulaþtýðý:<br>
<ul>
   <li>(yanýtlamayan) - $nasilulasti_sayisi{0}
   <li>$nasilulasti{1} - $nasilulasti_sayisi{1}
   <li>$nasilulasti{2} - $nasilulasti_sayisi{2}
   <li>$nasilulasti{3} - $nasilulasti_sayisi{3}
   <li>$nasilulasti{4} - $nasilulasti_sayisi{4}
   <li>$nasilulasti{5} - $nasilulasti_sayisi{5}
   <li>$nasilulasti{6} - $nasilulasti_sayisi{6}
</ul>

Kaç kiþinin hangi bilgisayar alanýyla ilgili olduðu:<br>
<ul>
   <li>Web Design: $ilgi{'wds'}
   <li>Web Server Yöneticiliði: $ilgi{'wsy'}
   <li>Electronic Commerce: $ilgi{'tic'}
   <li>Elektronik Ticaret: $ilgi{'tic'}
   <li>Ýnternet Aracýlýðýyla Eðitim: $ilgi{'egt'}
</ul><p>

Sayfa Hakkýnda Yorumlar:<p>
$yorumlar

HTMLSonu
;

sub hata {
   ($hatamesaji) = @_;
   print "<h2>Hata!</h2>\n";
   print $hatamesaji;
   exit;
}
