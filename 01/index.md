# 28. september 2017

## Thonny installimine
Ringis hakkame kasutama algajatele mõeldud programmeerimiskeskkonda Thonny. Installimiseks vajalikud failid saab aadressilt [http://thonny.org](http://thonny.org).

## Tere, maailm!

Kopeeri Thonnysse järgnev tekst ja vajuta F5:

```python
print('Tere, maailm!')
```

## Kilpkonn
Lisaks teksti väljastamisele on Pythonis väga lihtne ka joonistada:

```python
from turtle import *

# liigu koos joonistamisega
forward(100) # liigu 100 sammu
left(90)     # pööra 90 kraadi
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)

# liigu kõrvale ilma joonistamata
up()          # tõsta pliiats
forward(200)  # liigu
down()        # pliiats tagasi alla

# uus joonistus
forward(30)
left(120)
forward(30)
left(120)
forward(30)
left(120)

done()
```

## Veebiprogrammid
[https://www.pythonanywhere.com](https://www.pythonanywhere.com) on sait, kuhu on võimalik tasuta üles panna Pythonis kirjutatud veebiprogramme.

```python
from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def tervitus():
    nimi  = request.args.get("nimi")
    vanus = request.args.get("vanus", type=int)

    # Reageeri vastavalt vanusele
    if vanus < 20:
        return 'Tere, ' + nimi + '!'
    else:
        return ('Olge tervitatud, lugupeetud '
              + nimi + '! Kas soovite istuda?')
```

### Demo

* [https://aivarannamaa.pythonanywhere.com/?nimi=Aivar&vanus=38](https://aivarannamaa.pythonanywhere.com/?nimi=Aivar&vanus=38)
* [https://aivarannamaa.pythonanywhere.com/?nimi=Mari&vanus=12](https://aivarannamaa.pythonanywhere.com/?nimi=Mari&vanus=12)

<div style="background-color:white; padding:20px; margin:10px">
<h3>Sisesta andmed ja vajuta nuppu</h3>
<form action="https://aivarannamaa.pythonanywhere.com/">
  <table border="0">
  <tr><td>Nimi</td><td><input type="text" name="nimi"></td></tr>
  <tr><td>Vanus</td><td><input type="number" name="vanus"></td></tr>
  </table>
  <input type="submit" value="Saada">
</form> 
</div>

## Veel näiteid
[https://github.com/progering/progering.github.io/tree/master/01](https://github.com/progering/progering.github.io/tree/master/01)

## Teeme ise arvutimänge

Tartu Ülikool korraldab [veebikursuse, kus õpetatakse Pythoniga arvutimängude loomist](https://courses.cs.ut.ee/2017/TIAM/fall/Main/HomePage).

**NB! Kuigi ametlik registreerumine on lõppenud, on ringis osalejatel veel võimalik ka selle kursusega liituda. Huvi korral kirjuta [aivar.annamaa@ut.ee](mailto:aivar.annamaa@ut.ee)!**

## Lisamaterjal

Kel rohkem huvi, võib uurida Tartu Ülikooli arvutiteaduse instituudi [programmeerimise õpikut](http://progeopik.cs.ut.ee).

## Küsimused
[aivar.annamaa@ut.ee](mailto:aivar.annamaa@ut.ee)

