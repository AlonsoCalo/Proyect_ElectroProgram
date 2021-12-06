import turtle
from turtle import *

title('Amplificador no inversor')
speed(5)

#Tierra 1
forward(15)
penup()
left(45)
forward(10)
left(135)
pendown()
forward(35)
penup()
right(45)
forward(10)
right(135)
pendown()
forward(55)
backward(27.5)

#Antes de fuente
left(90)
forward(30)
right(90)

#Fuente
circle(15)
penup()
left(90)
forward(30)
pendown()

#Pre R1
forward(40)
right(90)
forward(40)

#Resistencia 1
left(75)
forward(10)
right(145)
forward(20)
left(145)
forward(20)
right(145)
forward(20)
left(145)
forward(20)
right(145)
forward(20)
left(145)
forward(10)
right(75)

#Post R1
forward(40)

#Amplificador
left(90)
forward(20)
right(120)
forward(80)
right(120)
forward(80)
right(120)
forward(60)

#Pre R2
left(90)
forward(20)
right(90)
forward(60)
right(90)
forward(40)

#Resistencia 2
left(75)
forward(10)
right(145)
forward(20)
left(145)
forward(20)
right(145)
forward(20)
left(145)
forward(20)
right(145)
forward(20)
left(145)
forward(10)
right(75)

#Post R2
forward(40)
right(90)
forward(80)
right(90)
backward(30)
forward(60)

penup()
forward(67)
left(90)
forward(20)
pendown()
right(90)
forward(30)
left(90)
forward(60)

#Tierra 2
right(90)
backward(27.5)
forward(55)
left(135)
penup()
forward(10)
pendown()
left(45)
forward(35)
right(135)
penup()
forward(10)
pendown()
right(45)
forward(15)

#Hacia tierra 3
right(180)
penup()
forward(128)
pendown()

#Tierra 3
forward(15)
penup()
left(45)
forward(10)
left(135)
pendown()
forward(35)
penup()
right(45)
forward(10)
right(135)
pendown()
forward(55)
backward(27.5)

left(90)
forward(50)

#Hacia los signos
penup()
forward(10)
left(90)
forward(84)

#Signo positivo
pendown()
forward(8)
backward(4)
right(90)
backward(4)
forward(8)

penup()
forward(36)
pendown()

#Signo negativo
left(90)
forward(4)
backward(8)

turtle.exitonclick()