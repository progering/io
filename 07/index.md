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

# 9. november 

Kohal 10 õpilast.

Panime kokku ruutvõrrandi lahendamise programmi

## Tunnis tehtud lahendus

```python
from math import sqrt

a = int(input("A="))
b = int(input("B="))
c = int(input("C="))

print(str(a) + "x²+" + str(b) + "x+" + str(c) + "=0")

D = b**2 - 4*a*c

if D < 0:
    print("Lahend puudub")
else:
    x1 = (-b + sqrt(D)) / (2*a)
    x2 = (-b - sqrt(D)) / (2*a)

    if x1 == x2:
        print("Ainuke lahend on", x1)
    else:
        print("1. lahend:", x1)
        print("2. lahend:", x2)
```

## Veebiprogramm

```python
from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def tervitus():
    from math import sqrt

    a = request.args.get("a", type=int)
    b = request.args.get("b", type=int)
    c = request.args.get("c", type=int)

    vorrand = str(a) + "x²+" + str(b) + "x+" + str(c) + "=0"

    D = b**2 - 4*a*c

    if D < 0:
        lahendid = "Lahend puudub"
    else:
        x1 = (-b + sqrt(D)) / (2*a)
        x2 = (-b - sqrt(D)) / (2*a)

        if x1 == x2:
            lahendid = "Ainuke lahend on "  + str(x1)
        else:
            lahendid = "1. lahend: " + str(x1) + "<br/>2. lahend: " + str(x2)

    return ("<h1>Võrrand</h1>\n" + vorrand
        + "\n<h1>Lahendid</h1>\n" + lahendid)

```

## Veebiprogrammi poole pöördumise näited

* [http://aivarannamaa.pythonanywhere.com/?a=3&b=-4&c=-4](http://aivarannamaa.pythonanywhere.com/?a=3&b=-4&c=-4)
* [http://aivarannamaa.pythonanywhere.com/?a=1&b=4&c=4](http://aivarannamaa.pythonanywhere.com/?a=1&b=4&c=4)
* [http://aivarannamaa.pythonanywhere.com/?a=1&b=4&c=14](http://aivarannamaa.pythonanywhere.com/?a=1&b=4&c=14)
* URL-i võid panna kokku ka alloleva vormi abil:

<div style="background-color:white; padding:20px; margin:10px">
<h3>Sisesta andmed ja vajuta nuppu</h3>
<form action="https://aivarannamaa.pythonanywhere.com/">
  <table border="0">
  <tr><td>a</td><td><input type="number" name="a"></td></tr>
  <tr><td>b</td><td><input type="number" name="b"></td></tr>
  <tr><td>c</td><td><input type="number" name="c"></td></tr>
  </table>
  <input type="submit" value="Arvuta">
</form> 
</div>


