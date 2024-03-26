# Test calc

**Uzdevums**  
Uzrakstīt katrai programmai manuālās testēšanas scenārijus.

1x Happy path  
Acīmredzams programmas izmantošanas piemērs

5x Use case  
Ietvert piemērus kā var būt lietota programma, kādos nolukos

5x Edge case  
Ietvērt robežgadījumus, nekorrektus izmantošanas piemērus

**Scenārija konstrukcija**  
Given -> When -> Then  
Priekšnosacījums -> Ievaddati -> Izvaddati

e.g. Zinot ka kurss ir 1.0831, padodot 10 eur, rezultāts būs 10.83 usd

**Edge case pārbaudes idejas**  
Decimālais ievads: Lietotājs ievada daļēju eiro daudzumu konvertēšanai (piemēram, 10,50 EUR).  
Negatīvs ievads: Lietotājs ievada negatīvu eiro daudzumu konvertēšanai.  
Noapaļošanas kļūdas: Lietotne sastop noapaļošanas kļūdas konvertēšanas procesā, kas izraisa neatbilstības konvertētajā summas.  
Valūtas simbola ievads: Lietotājs iekļauj eiro simbolu (€) kopā ar daudzumu konvertēšanai.  
Lokālas savietojamības: Lietotājs no reģiona, kur decimālo atdalītāju vai tūkstošgadu atdalītāju atšķiras no standarta ievades formāta, mēģina veikt konvertēšanu.  
Laika beigas: Lietotne neizdodas iegūt valūtas kursu noteiktajā laika limitā sakarā ar lēnu tīklu vai servera problēmām.  
Nederīgs valūtas kursa: Iegūtais valūtas kurss ir nederīgs vai novecojis, izraisot neprecīzu konvertāciju.  

  
** Dokumentācija Unit Testiem**  
https://docs.python.org/3/library/unittest.html#assert-methods