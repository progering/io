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

# 12. oktoober 2017

Kohal 9 õpilast.

## Kilpkonnagraafika

```python
from turtle import *

speed(10)
delay(0)

# Joonistan teljed
goto(0, -100)
goto(0, 100)
goto(0,0)
goto(-100, 0)
goto(100, 0)
up()

# Ruutfunktsiooni graafik
x = -15
while x <= 15:
    y = 0.2*(x**2) - 5
    goto(x*10, y*10)
    
    if y < 0:
        pencolor("blue")
    else:
        pencolor("red")
    
    dot()
    
    x = x + 0.1


mainloop()
```

## Korrutamine liitmise kaudu

```python
a = 48
b = 167
# Korrutis kasutades korrutamistehet
print(a * b)

# Korrutis ilma korrutamistehet kasutamata
# 167 + 167 + 167 + ...
summa = 0
while a > 0:
    summa = summa + b
    a = a - 1

print(summa)
```