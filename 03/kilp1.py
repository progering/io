from turtle import *

a = 1
b = 0 
c = 0

x = -5

up()
while x < 5:
    y = a*x**2 + b*x + c
    goto(x*10, y*10)
    dot()
    
    x += 0.1
     
  