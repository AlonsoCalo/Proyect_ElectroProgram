import turtle
from turtle import *

title('Amplificador Sumador')
speed(9)

#Diagrama a la izquierda
penup()
backward(280)
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
forward(250)

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
backward(40)
right(90)
forward(40)
right(90)
forward(20)

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
forward(170)
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
forward(40)

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
backward(7.5)
right(90)
forward(115)
right(90)
forward(226)
right(90)

pendown()
forward(40)
right(90)
forward(20)

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
forward(90)
left(90)
forward(30)

#Fuente 3
right(90)
circle(15)

#Post fuente 3
penup()
left(90)
forward(30)
pendown()
forward(40)

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

#De regreso
penup()
right(180)
forward(154)
left(90)
forward(197)
right(90)
forward(40)
pendown()

#Triangulo
left(90)
forward(20)
right(120)
forward(80)
right(120)
forward(80)
right(120)
forward(60)

#Post Triangulo
penup()
left(90)
forward(20)
pendown()
right(90)
forward(60)
right(90)
forward(30)

#Resistencia f
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

#Post Rf
forward(40)
right(90)
forward(82)
right(90)
forward(19)
backward(38)
left(90)
forward(20)

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

#Tierra 5
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
forward(14)
right(90)
forward(90)
left(90)
forward(85)
left(90)
forward(20)
pendown()
right(90)
forward(20)
left(90)
forward(80)

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

#A los signos
penup()
right(180)
forward(38)
left(90)
forward(90)
pendown()


#Signo positivo
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
