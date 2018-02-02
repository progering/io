[<< Avaleht](/)

<style>
.pre {
    font-family: monospace;
    white-space: pre;
}

aside.notice {
    background-color:#fffed6;
    border-color: black;
    border-width: 1px;
    padding: 10px;
    margin-bottom: 20px;
}

</style>

# 8. veebruar

Hakkame tegelema veebiprogrammidega!

## Lingid

* [https://www.pythonanywhere.com/](https://www.pythonanywhere.com/)
* [HTML-i veebikursus](https://www.codecademy.com/tracks/web-et)
* [HTML-i redaktor](https://html-online.com/editor/)

## Pythonanywhere

1. Loo endale konto
2. Vali ülevalt-paremalt "Web"
3. Klõpsa "Add a new web app"
4. "Your web app's domain name" -- selle jätame vahele. Klõpsa "Next"
5. "Select a Python Web framework" -- vali "Flask" 
6. "Select a Python version" -- vali "Python 3.6"
7. "Quickstart new Flask project" -- ära muuda midagi ja klõpsa "Next"
8. Nüüd peaksid nägema oma veebisaidi konfigureerimislehte pealkirjaga **"Configuration for _sinu nimi_.pythonanywhere.com"**. Ava pealkirjas olev link uuel tabil. Peaksid nägema oma veebilehte, mille sisuks on **"Hello from Flask!"**
9. Mine tagasi oma veebisaidi konfigureerimiselehele ja otsi üles pealkiri **"Code"**. Selle all on rida, mis algab tekstiga **"Source code"**. Klõpsa selle rea lõpus olevat linki **"Go to directory"**.
10. Klõpsa uuel lehel paremal poolel olevat linki **"flask_app.py"**.
11. Ilmub koodiredaktor, kus on näha veebilehe koodi. Kirjuta koodis sõne `'Hello from Flask!'` asemel `'<h1>Tere!</h1>Testin, testin ...'`.
12. Vajuta ülevalt-paremalt rohelist Save nuppu (või Ctrl+S) ja peale seda Reload nuppu (kahe kõvera noolega).
13. Mine tagasi oma veebilehele ja lae lehekülg uuesti (F5). Peaksid nägema koodis tehtud muudatust.

## HTML

HTML on veebilehtede loomise keel, kus tavalise teksti vahele pikitakse spetsiaalseid märgendeid, mis muudavad märgendite vahel oleva teksti tähendust. Näiteks
`'<h1>Tere!</h1>Testin, testin ...'` puhul on tekst "Tere" paigutatud märgendite `<h1>` ja `</h1>` vahele, mis tähistavad 1. taseme pealkirja. See on põhjus, miks brauser näidab "Tere!" suures kirjas ja eraldi real.

Lihtsamate veebilehtede korral kirjutataksegi kogu veebileht HTML keeles valmis (tavaliselt .html laiendiga tekstifaili) ja laetakse serverile üles. Selliseid veebilehti nimetatakse *staatilisteks* -- brauser näitab neid alati samasugusena.

Veebilehti võib teha ka *dünaamiliseks*. Sel juhul peab kusagil olema mingi programm, mis vastavalt mingitele tingimustele tekitab üht või teistsugust HTML koodi. Meie näites oli see programm kirjutatud Pythonis ja asus failis "flask_app.py". Hetkel oli tulemus küll alati samasugune, aga soovi korral saaksime programmi täiendada ja panna tulemuseks antava HTML-i sõltuma millest iganes.

Dünaamiliste veebilehtede juurde tuleme hiljem tagasi, aga esmalt hakkame õppima HTML-i põhimõtteid. Selleks tekitame Pythonanywhere projektis eraldi kausta staatiliste lehtede jaoks.

1. Mine tagasi sellele lehele, kus näidati "flask_app.py" koodi. Lehekülje üleval-vasakul peaks olema midagi sellist: **"/home/_sinu nimi_/mysite/flask_app.py"**. Klõpsa seal lingi **"mysite"** peale.
2. Nüüd peaks ilmuma lehekülg, mis näitab veebisaidi peakausta. Vasakul on kast, kuhu on kirjutatud "Enter new directory name". Kirjuta sinna "static" ja vajuta nuppu "New directory". See tekitab uue kausta, mis sobib staatiliste HTML failide hoidmiseks.
3. Uuel lehel otsi paremalt kast kirjaga "Enter new file name ...". Kirjuta sinna **"katsetus.html"** ning vajuta nuppu "New file". 
4. Seepeale peaks ilmuma faili redaktor. Kopeeri sinna järgnev tekst ja salvesta:

```
<!DOCTYPE html>
<html>
<head>
<title>Esimene tõsisem katsetus</title>
</head>

<body>
<h1>See on 1. taseme pealkiri</h1>
Mingi <b>jutt</b>. Mingi <a href="http://tdk.ee">link</a>
<h2>See on 2. taseme pealkiri</h2>
Veel mingi jutt.

Loetelu:
<ul>
    <li>essa</li>
    <li>tessa</li>
    <li>kossa</li>
</ul>

Pilt: <img src="http://portal.tdl.ee/images/pagemaster/kool1c.jpg"/>
</body>
</html>
```

Mine nüüd aadressile **https://_sinu nimi_.pythonanywhere.com/static/katsetus.html** ja uuri, kuidas brauser seda lehte näitab.

Selles näites on märgendeid juba rohkem. Mõned neist (`<!DOCTYPE html>`, `<html>`, `<head>`, `<body>`) ei ole brauseris otseselt nähtavad, aga need peavad korrektses veebilehes siiski olemas olema.

## Codecademy

HTML-i põhimõtete õppimiseks jätame nüüd Pythonanywhere'i mõneks ajaks kõrvale ja võtame ette ühe veebikursuse.

Mine lehele [https://www.codecademy.com/tracks/web-et](https://www.codecademy.com/tracks/web-et), tee seal endale konto ja järgi edasisi juhiseid.


