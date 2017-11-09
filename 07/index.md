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

## Failide lugemine ja kirjutamine

Pythonis on lihtne lugeda andmeid tekstifailist või neid sinna kirjutada.

Täpsemalt saab sõnedest lugeda [siit](http://progeopik.cs.ut.ee/02_lihtlaused.html#failide-lugemine-reakaupa).

### Failist kindlate ridade lugemine

```python
f = open('andmed.txt')

nimi = f.readline()
vanus = f.readline()
aadress = f.readline()

print("Nimi:", nimi)
print("Vanus:", vanus, "aastat")
print("Aadress:", aadress)

f.close()
```

### Failist lugemine reakaupa, kui ridade arv pole teada

```python
f = open('andmed.txt')

while True:
    rida = f.readline()
    
    if rida == '':
        break
    
    print(rida)

f.close()
```

### Faili sisu korraga lugemine

```python
f = open('tekst.txt')
faili_sisu = f.read()
print(faili_sisu)
f.close()
```

### Faili kirjutamine
```python
nimi = input("Palun sisesta oma nimi: ")
vanus = input("vanus: ")
aadress = input("aadress: ")

f = open("andmed2.txt", "w")
f.write(nimi + "\n")
f.write(vanus + "\n")
f.write(aadress + "\n")
f.close()
```


### Näide
Programm loeb failist temperatuuri Fahrenheiti skaalal ja väljastab selle Celsiuse skaalal

```python
f = open('fahrenheit.txt')

temp_f = float(f.readline())
temp_c = (temp_f - 32) * (5/9)

print(temp_f, "on Celsiuse skaalal", temp_c)

f.close()
```

### Harjutus 1
Kirjuta eelnevale näitele vastupidine programm, mis loeb failist `celsius.txt` ühe Celsiuse temperatuuri, ning väljastab (st. prindib) selle Fahrenheiti skaalal.

### Harjutus 2
Muuda eelmist programmi nii, et see töötaks õigesti mitmerealiste failidega -- igalt realt tuleb lugeda Celsiuse temperatuur ja väljastada see Fahrenheiti skaalal.

Programm peaks töötama suvalise arvu ridade korral.