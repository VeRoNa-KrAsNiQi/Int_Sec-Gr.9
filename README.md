# Int_Sec-Gr.9


<h1 align="center">XSS-SCANNER</h1>   

## Çka është Cross-Site Scripting

Sulmet Cross-Site Scripting (XSS) janë një lloj injeksioni, në të cilin skriptet me qëllim të keq injektohen në web aplikacione të ndryshme. Sulmet XSS ndodhin kur një sulmues përdor një aplikacion në internet për të dërguar kodin me qëllim të keq. Të metat që lejojnë që këto sulme të kenë sukses janë mjaft të përhapura dhe ndodhin kudo ku një web aplikacion me nivel të ulët sigurie.
Një sulmues mund të përdorë XSS për të dërguar një skript me qëllim të keq tek një përdorues që nuk dyshon. Shfletuesi i përdoruesit nuk ka asnjë mënyrë për të ditur se skripti nuk duhet të besohet, prandaj do ta ekzekutojë skriptin. Për shkak se ai mendon se skripti ka ardhur nga një burim i besuar, skripti keqdashës mund të ketë çasje në çdo skedar "cookie", "sessions" ose informacione të tjera sensitive të ruajtura nga shfletuesi dhe të përdorura me atë faqe. Këto skripta madje mund të rishkruajnë përmbajtjen e faqes HTML.


### LLojet e Cross-Site Scripting

Ekzistojnë 3 lloje kryesore të sulmeve XSS:
    <br />  1.Stored XSS
    <br />  2.Reflected XSS
    <br />  3.Dom-based XSS

**Stored XSS** - lejon një sulmues të injektojë një skrip me qëllim të keq, zakonisht ne forma ku kerkohen te dhenat e perdoruesit.Kjo skripte ruhet ne web serverin i cili ka siguri te ulet dhe viktima mund te jene
te gjithe ata perdorues qe e vizitojne webfaqen.

**Reflected XSS** - ndodh kur nje skript me qellim te keq reflektohet nga nje aplikacion ne internet ne shfletuesin e viktimes.
Skripti aktivizohet përmes një lidhjeje, e cila dërgon një kërkesë në një faqe interneti te cenueshme që mundëson ekzekutimin e ketyre skriptave.Dobësia është zakonisht rezultat i inputeve hyrëse që nuk janë sanitizuar mjaftueshëm, gjë që lejon manipulimin e funksioneve të një aplikacioni në internet dhe aktivizimin e skriptave.

**Dom-based XSS** - është i mundur nëse aplikacioni në internet shkruan të dhëna në DOM (Document Object Model) pa sanitizimin e duhur. Sulmuesi i manipulon këto të dhëna për të përfshirë përmbajtjen e skriptave maliciose.
Rreziku kryesor i ketij sulmi eshte qe sulmuesi mundet te kete casje edhe ne source kodin e webfaqes.


## Funksionimi i XSS-Scanner 

XSS Scanner është aplikacion i ndërtuar për detektimin e Cross-Site Skripatve që mund të ekzistojnë në ndonjë web applikacion, URL-ja e të cilit shënohet në textbox. Ky aplikacion u ndërtua mbi gjuhën progamuese Python dhe është përdorur textfile Payloads i cili përmban skriptat e mundshme malicioze. 
Graphical User Interface (GUI) i applikacionit XSS Scanner

![271197196_327868739342036_1124851856919966101_n](https://user-images.githubusercontent.com/75573960/148659642-64ec066a-7a08-422b-946e-a98c5163722d.png)



Pamje e aplikacionit në rastet kur kemi një URL jo reale apo kur shtyp butonin "Scan" përderisa textbox-i është i zbrazët.

![271219227_5000910409930624_2894316500571681692_n](https://user-images.githubusercontent.com/75573960/148659665-56726a6b-c125-48c8-ad0f-3cdff740191b.png)




Pamje e aplikacionit kur në textbox shkruhet një URL reale e cila është e sigurtë dhe nuk përmban
ndonjë skriptë malicioze. 

![271492490_2920538284925726_6135089769111100551_n](https://user-images.githubusercontent.com/75573960/148659684-f6ef0478-fcb1-4d8c-9d24-62f93df4588c.png)




Pamje e aplikacionit në rastet kur website-i që korrespondon me URL-në e dhënë përmban skripta malicioze.

![271518349_1092490984624682_4608459445773184234_n](https://user-images.githubusercontent.com/75573960/148659693-6258b13e-26fd-4417-a567-8023d4b634b5.png)






 




