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

# 05. oktoober 2017

Kohal 6 õpilast. 

## Arvud
Pythonis tehakse vahet **täisarvudel** (nt. `-2` või `889887575465463`) ja **ujukomaarvudel**, mida võib nimetada ka murdarvudeks (nt. `3.14`).

<aside class="notice">
NB! Ujukomaarvude täis- ja murdosa vahele käib <b>punkt</b>, mitte koma. Komal on Pythonis teine tähendus.
</aside>

### Tehted arvudega
<table border="1" class="docutils">
<colgroup>
<col width="23%" />
<col width="11%" />
<col width="66%" />
</colgroup>
<thead valign="bottom">
<tr class="row-odd"><th class="head">Avaldis</th>
<th class="head">Väärtus</th>
<th class="head">Selgitus</th>
</tr>
</thead>
<tbody valign="top">
<tr class="row-even"><td><code class="docutils literal"><span class="pre">6</span> <span class="pre">/</span> <span class="pre">3</span></code></td>
<td><code class="docutils literal"><span class="pre">2.0</span></code></td>
<td>Tavalise jagamise tulemus on alati ujukomaarv</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">5</span> <span class="pre">//</span> <span class="pre">3</span></code></td>
<td><code class="docutils literal"><span class="pre">1</span></code></td>
<td>Täisarvuline jagamine</td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">5</span> <span class="pre">%</span> <span class="pre">3</span></code></td>
<td><code class="docutils literal"><span class="pre">2</span></code></td>
<td>Jagamise jäägi leidmine</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">5</span> <span class="pre">**</span> <span class="pre">3</span></code></td>
<td><code class="docutils literal"><span class="pre">125</span></code></td>
<td>Astendamine</td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">4</span> <span class="pre">**</span> <span class="pre">0.5</span></code></td>
<td><code class="docutils literal"><span class="pre">2.0</span></code></td>
<td>Juurimine astendamise kaudu</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">round(2.6375,</span> <span class="pre">2)</span></code></td>
<td><code class="docutils literal"><span class="pre">2.64</span></code></td>
<td>Ümardamine nõutud täpsusega</td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">round(2.6375)</span></code></td>
<td><code class="docutils literal"><span class="pre">3</span></code></td>
<td>Ümardamine lähima täisarvuni</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">int(2.6375)</span></code></td>
<td><code class="docutils literal"><span class="pre">2</span></code></td>
<td>Täisarvuks teisendades ei ümardata</td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">3</span> <span class="pre">+</span> <span class="pre">5</span> <span class="pre">*</span> <span class="pre">2</span></code></td>
<td><code class="docutils literal"><span class="pre">13</span></code></td>
<td rowspan="2">Python arvestab tehete järjekorda</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">(3</span> <span class="pre">+</span> <span class="pre">5)</span> <span class="pre">*</span> <span class="pre">2</span></code></td>
<td><code class="docutils literal"><span class="pre">16</span></code></td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">6</span> <span class="pre">-</span> <span class="pre">3</span> <span class="pre">-</span> <span class="pre">1</span></code></td>
<td><code class="docutils literal"><span class="pre">2</span></code></td>
<td rowspan="2">Sama prioriteediga tehted tehakse vasakult paremale ...</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">6</span> <span class="pre">-</span> <span class="pre">(3</span> <span class="pre">-</span> <span class="pre">1)</span></code></td>
<td><code class="docutils literal"><span class="pre">4</span></code></td>
</tr>
<tr class="row-even"><td><code class="docutils literal"><span class="pre">2</span> <span class="pre">**</span> <span class="pre">3</span> <span class="pre">**</span> <span class="pre">2</span></code></td>
<td><code class="docutils literal"><span class="pre">512</span></code></td>
<td rowspan="2">... v.a astendamised, mis tehakse paremalt vasakule</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal"><span class="pre">(2</span> <span class="pre">**</span> <span class="pre">3)</span> <span class="pre">**</span> <span class="pre">2</span></code></td>
<td><code class="docutils literal"><span class="pre">64</span></code></td>
</tr>
</tbody>
</table>

### Moodul math

Suur hulk matemaatilisi funktsioone ja konstante on kättesaadavad peale seda, kui need *importida* moodulist nimega `math`:

```python
>>> from math import *
>>> cos(pi * 1.5)
-1.8369701987210297e-16
>>> atan(0.5)
0.4636476090008061
>>> radians(360)
6.283185307179586
>>> 2 * pi
6.283185307179586
>>> degrees(2*pi)
360.0
>>> log(10.0)
2.302585092994046
>>> log(e)
1.0
>>> log(100,10)
2.0
>>> sqrt(9)
3.0
```

### Harjutus
Väärtusta Pythoni käsureal järgmised avaldised:

* ![](sqrt.svg)
* ![](aste.svg)

### Tunnis tehtud näidisprogramm
```python
from random import randint

õigeid_vastuseid = 0
while True:
    x = randint(1, 10)
    y = randint(1, 10)
    õige_vastus = x + y

    print("Tehe on", x, "+", y)
    kasutaja_vastus = int(input("Sisesta vastus: "))

    if kasutaja_vastus == õige_vastus:
        print("Tubli!")
        õigeid_vastuseid = õigeid_vastuseid + 1
    else:
        print("Vale! Õige vastus on", õige_vastus)
        print("Vastasid õigesti", õigeid_vastuseid, "korda")
        break

print("tadaa!")


```


## Täpsemalt
[Samad teemad programmeerimise õpikus](http://progeopik.cs.ut.ee/02_lihtlaused.html#soned)
