import turtle
from turtle import *

title('Amplificador de Diferencia')
speed(7)

#Diagrama a la izq.
penup()
backward(200)
pendown()

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

#Fuente 1
backward(27.5)
left(90)
forward(40)
right(90)
circle(15)

#Antes de R1
penup()
left(90)
forward(30)
pendown()
forward(40)
right(90)
forward(230)

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
forward(60)
backward(30)
right(90)
penup()
forward(40)
right(90)
pendown()
backward(30)
forward(60)

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
forward(150)
left(90)
forward(30)

#Fuente 2
right(90)
circle(15)

#Post fuente 2
penup()
left(90)
forward(30)
pendown()
forward(30)

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

#De regreso
penup()
right(180)
forward(230)
left(90)
forward(106)
forward(40)
right(90)
forward(25)

#Triangulo
pendown()
left(90)
forward(20)
right(120)
forward(80)
right(120)
forward(80)
right(120)
forward(60)

#Post triangulo
left(90)
forward(30)
right(90)
forward(60)
right(90)
forward(30)

#Resistencia 3
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

#Post R3
forward(53)
right(90)
forward(82)
right(90)
forward(19)
backward(38)
left(90)
forward(40)

#Resistencia L
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

#Post Rl
forward(20)

#Tierra 4
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

#De regreso
penup()
forward(132)
right(90)
forward(91)
pendown()
right(180)
forward(30)

#Resistencia 4
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

#Post R4
forward(20)

#Tierra 3
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

#A los signos
penup()
right(180)
forward(45)
left(90)
forward(96)

#Signo positivo
pendown()
forward(8)
backward(4)
left(90)
forward(4)
backward(8)

penup()
forward(4)
right(90)
forward(40)
pendown()

#Signo negativo

left(90)
forward(4)
backward(8)




turtle.exitonclick()
