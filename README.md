# Int_Sec-Gr.9


## Çka është Cross-Site Scripting

Sulmet Cross-Site Scripting (XSS) janë një lloj injeksioni, në të cilin skriptet me qëllim të keq injektohen në web aplikacione të ndryshme. Sulmet XSS ndodhin kur një sulmues përdor një aplikacion në internet për të dërguar kodin me qëllim të keq. Të metat që lejojnë që këto sulme të kenë sukses janë mjaft të përhapura dhe ndodhin kudo ku një web aplikacion me nivel të ulët sigurie.
Një sulmues mund të përdorë XSS për të dërguar një skript me qëllim të keq tek një përdorues që nuk dyshon. Shfletuesi i përdoruesit nuk ka asnjë mënyrë për të ditur se skripti nuk duhet të besohet, prandaj do ta ekzekutojë skriptin. Për shkak se ai mendon se skripti ka ardhur nga një burim i besuar, skripti keqdashës mund të ketë çasje në çdo skedar "cookie", "sessions" ose informacione të tjera sensitive të ruajtura nga shfletuesi dhe të përdorura me atë faqe. Këto skripta madje mund të rishkruajnë përmbajtjen e faqes HTML.


### LLojet e Cross-Site Scripting

Ekzistojnë 3 lloje kryesore të sulmeve XSS:
      1.Stored XSS
      2.Reflected XSS
      3.Dom-based XSS

**Stored XSS** - lejon një sulmues të injektojë një skrip me qëllim të keq, zakonisht ne forma ku kerkohen te dhenat e perdoruesit.Kjo skripte ruhet ne web serverin i cili ka siguri te ulet dhe viktima mund te jene
te gjithe ata perdorues qe e vizitojne webfaqen.

**Reflected XSS** - ndodh kur nje skript me qellim te keq reflektohet nga nje aplikacion ne internet ne shfletuesin e viktimes.
Skripti aktivizohet përmes një lidhjeje, e cila dërgon një kërkesë në një faqe interneti te cenueshme që mundëson ekzekutimin e ketyre skriptave.Dobësia është zakonisht rezultat i inputeve hyrëse që nuk janë sanitizuar mjaftueshëm, gjë që lejon manipulimin e funksioneve të një aplikacioni në internet dhe aktivizimin e skriptave.

**Dom-based XSS** - është i mundur nëse aplikacioni në internet shkruan të dhëna në DOM (Document Object Model) pa sanitizimin e duhur. Sulmuesi i manipulon këto të dhëna për të përfshirë përmbajtjen e skriptave maliciose.
Rreziku kryesor i ketij sulmi eshte qe sulmuesi mundet te kete casje edhe ne source kodin e webfaqes.


