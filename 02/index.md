[<< Avaleht](/)

<style>
.pre {
    font-family: monospace;
    white-space: pre;
}
</style>

# 04. oktoober 2017

## Tehted arvudega

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