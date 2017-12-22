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

# 2. november 

Kohal 9 õpilast.

## Sõned

Sõned on tekstijupid, mis kirjutatakse Pythoni koodis ülakomade või jutumärkide vahele.

Täpsemalt saab sõnedest lugeda [siit](http://progeopik.cs.ut.ee/02_lihtlaused.html#soned)

### Sõneoperatsioonid
<table border="1" class="docutils">
<colgroup>
<col width="29%" />
<col width="16%" />
<col width="55%" />
</colgroup>
<thead valign="bottom">
<tr class="row-odd"><th class="head">Avaldis</th>
<th class="head">Väärtus</th>
<th class="head">Selgitus</th>
</tr>
</thead>
<tbody valign="top">
<tr class="row-even"><td><code class="docutils literal"><span class="pre">'Tere'</span> <span class="pre">+</span> <span class="pre">'Madis!'</span></code></td>
<td><code class="docutils literal"><span class="pre">'TereMadis!'</span></code></td>
<td><code class="docutils literal"><span class="pre">+</span></code> loob kahe sõne põhjal uue sõne</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">'Tere'</span> <span class="pre">+</span> <span class="pre">'</span> <span class="pre">Madis!'</span></code></td>
<td><code class="docutils literal"><span class="pre">'Tere</span> <span class="pre">Madis!'</span></code></td>
<td>Tühikud tuleb vajadusel ise vahele panna</td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">'Tere'</span> <span class="pre">+</span> <span class="pre">'</span> <span class="pre">'</span> <span class="pre">+</span> <span class="pre">'Mad'</span> <span class="pre">+</span> <span class="pre">'is!'</span></code></td>
<td><code class="docutils literal"><span class="pre">'Tere</span> <span class="pre">Madis!'</span></code></td>
<td>Kokku võib liita ka mitu sõnet</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">'nr.'</span> <span class="pre">+</span> <span class="pre">1</span></code></td>
<td>Viga!!!</td>
<td>Sõnet ja arvu ei saa niisama ühendada</td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">'nr.'</span> <span class="pre">+</span> <span class="pre">str(1)</span></code></td>
<td><code class="docutils literal"><span class="pre">'nr.1'</span></code></td>
<td><code class="docutils literal"><span class="pre">str</span></code> annab arvule vastava sõne</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">'5'</span> <span class="pre">+</span> <span class="pre">'3'</span></code></td>
<td><code class="docutils literal"><span class="pre">'53'</span></code></td>
<td>Sõnena esitatud arve ei käsitleta arvudena</td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">int('5')</span></code></td>
<td><code class="docutils literal"><span class="pre">5</span></code></td>
<td><code class="docutils literal"><span class="pre">int</span></code> annab sõnele vastava täisarvu</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">float('5.3')</span></code></td>
<td><code class="docutils literal"><span class="pre">5.3</span></code></td>
<td><code class="docutils literal"><span class="pre">float</span></code> annab sõnele vastava ujukomaarvu</td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">'xo'</span> <span class="pre">*</span> <span class="pre">3</span></code></td>
<td><code class="docutils literal"><span class="pre">'xoxoxo'</span></code></td>
<td>Sõne dubleerimine</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">len('tere')</span></code></td>
<td><code class="docutils literal"><span class="pre">4</span></code></td>
<td>Sõne pikkuse (<cite>length</cite>) küsimine</td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">'tere'.upper()</span></code></td>
<td><code class="docutils literal"><span class="pre">'TERE'</span></code></td>
<td rowspan="3">Mõnede käskude korral kirjutatakse sõne käsu ette.
Taolisi käske nimetatakse <em>meetoditeks</em>.</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">'TeRe'.lower()</span></code></td>
<td><code class="docutils literal"><span class="pre">'tere'</span></code></td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">'jäääär'.count('ä')</span></code></td>
<td><code class="docutils literal"><span class="pre">4</span></code></td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">'tere'.rjust(10)</span></code></td>
<td><code class="docutils literal"><span class="pre">'</span>&#160;&#160;&#160;&#160;&#160; <span class="pre">tere'</span></code></td>
<td rowspan="3">Sõne paigutamine etteantud &#8220;ruumi&#8221;, see on abiks nt tabelite
moodustamisel. Selle meetodi paariliseks on <code class="docutils literal"><span class="pre">ljust</span></code>, katseta ise,
mida see teeb!
Teise argumendiga saab määrata, millist sümbolit ruumi täitmiseks
kasutatakse.</td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">'terekest'.rjust(12)</span></code></td>
<td><code class="docutils literal"><span class="pre">'</span>&#160;&#160;&#160; <span class="pre">terekest'</span></code></td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">'terekest'.rjust(12,</span> <span class="pre">'~')</span></code></td>
<td><code class="docutils literal"><span class="pre">'~~~~terekest'</span></code></td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">'</span> <span class="pre">tere</span> <span class="pre">'.strip()</span></code></td>
<td><code class="docutils literal"><span class="pre">'tere'</span></code></td>
<td rowspan="2">Meetod <code class="docutils literal"><span class="pre">strip</span></code> annab sõne ilma alguses ja lõpus olevate tühikute
ja reavahetusteta</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">'tere'.strip()</span></code></td>
<td><code class="docutils literal"><span class="pre">'tere'</span></code></td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">'tere'.replace('e','ö')</span></code></td>
<td><code class="docutils literal"><span class="pre">'törö'</span></code></td>
<td rowspan="3">Meetod <code class="docutils literal"><span class="pre">replace</span></code> genereerib uue sõne, kus näidatud tähed või
<em>alamsõned</em> on asendatud millegi muuga.</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">'tere'.replace('a',</span> <span class="pre">'b')</span></code></td>
<td><code class="docutils literal"><span class="pre">'tere'</span></code></td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">'isamaa'.replace('isa',</span> <span class="pre">'ema')</span></code></td>
<td><code class="docutils literal"><span class="pre">'emamaa'</span></code></td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">'abc'[0]</span></code></td>
<td><code class="docutils literal"><span class="pre">'a'</span></code></td>
<td rowspan="3">Kirjutades sõne järele nurksulgudesse mingi numbri, antakse
vastuseks vastava järjekorranumbriga e <em>indeksiga</em> täht.
NB! Indeksid algavad 0-ga.</td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">'abc'[1]</span></code></td>
<td><code class="docutils literal"><span class="pre">'b'</span></code></td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">'abc'[2]</span></code></td>
<td><code class="docutils literal"><span class="pre">'c'</span></code></td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">'tere'[0:3]</span></code></td>
<td><code class="docutils literal"><span class="pre">'ter'</span></code></td>
<td rowspan="2">Kui nurksulgudesse kirjutada kooloniga eraldatult kaks indeksit,
siis antakse sõnest lõik alates esimesest indeksist (kaasaarvatud)
kuni viimase indeksini (väljaarvatud).</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">'tere'[2:4]</span></code></td>
<td><code class="docutils literal"><span class="pre">'re'</span></code></td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">'tere'.replace('e','ö').upper()</span></code></td>
<td><code class="docutils literal"><span class="pre">'TÖRÖ'</span></code></td>
<td>Käske saab kombineerida</td>
</tr>
</tbody>
</table>


### Harjutus. Kaja
Kirjuta programm, mis küsib kasutajalt sõna ja kuvab selle ekraanile suurte tähtedega:

```
Sisesta sõna: kapsas
KAPSAS
```

Nüüd muuda programmi nii, et sõnu küsitaks korduvalt. Sõnade küsimine lõppeb, kui kasutaja sisestab tühja sõne `""` (teisisõnu, vajutab lihtsalt ENTER-it):

```
Sisesta sõna: kapsas
KAPSAS
Sisesta sõna: Peeter
PEETER
Sisesta sõna:
Sisestasid tühja sõna, lõpetan töö.
```

Järgmiseks proovi nii, et programm väljastab sõna 3 korda -- esimesel korral suurte tähtedega, siis väikeste tähtedega ja lõpuks ainult sõna kaks esimest tähte (väikselt):

```
Sisesta sõna: kapsas
KAPSAS, kapsas, ka...
Sisesta sõna: Peeter
PEETER, peeter, pe...
Sisesta sõna:
Sisestasid tühja sõna, lõpetan töö.
```

Tunnis tehtud lahendus:
 
```python
while True:
    s = input("Sisesta sõna: ")
    if s == '':
        break
    print(s.upper()
          + ", " + s.lower()
          + ", " + s[0:2] + "...")
```



### Harjutus. Salasõna kontrollija
Kirjuta programm, mis küsib kasutajalt mingi sõna ja ütleb, kas see sobib salasõnaks.

Oletame, et salasõna kriteeriumid on järgmised:

* pikkus on vähemalt 8 sümbolit
* sisaldab nii suuri kui väikseid tähti
* ei tohi olla "jalgratas", "JalgRatas", "jalgRAtaS", jne...

```
Sisesta sõna: Keerukuju
Sõnas pole numbreid!
```

Tunnis tehtud lahendus:
```python
sõna = input("Sisesta soovitud salasõna: ")

if len(sõna) < 8:
    print("Ei sobi, parool on liiga lühike")
elif sõna.lower() == sõna:
    print("Ei sobi, kõik tähed on väikesed")
elif sõna.upper() == sõna:
    print("Ei sobi, kõik tähed on suured")
elif sõna.lower() == "jalgratas":
    print("Jalgratas ei sobi")
else:
    print("Sobib")
    

```
