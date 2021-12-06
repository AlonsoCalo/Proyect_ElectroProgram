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

#Antes de R1
backward(27.5)
left(90)
forward(120)
right(90)
forward(20)

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

#Continuacion resistencia 1
forward(40)
backward(20)
left(90)
forward(70)
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

#Despues de R2
forward(50)
right(90)
forward(100)
left(90)
forward(30)

#Tierra 3
right(90)
penup()
forward(50)
pendown()
forward(20)
right(90)
pendown()
forward(25.7)
backward(55)
left(45)
penup()
forward(10)
right(45)
pendown()
forward(35)
left(135)
penup()
forward(10)
left(45)
pendown()
forward(15)

#De regreso
penup()
backward(7.5)
left(90)
forward(83.5)
right(90)



#OpAmp
pendown()
backward(60)
left(145)
forward(90)
left(125)
forward(100)
left(125)
forward(90)

#De regreso del OpAmp
penup()
backward(90)
left(55)
forward(20)
left(90)
pendown()
forward(30)
left(90)
forward(30)
right(90)

#Fuente
circle(15)

#Linea despues de fuente
penup()
left(90)
forward(30)
pendown()
forward(30)

#Tierra 2
right(90)
forward(25.7)
backward(55)
left(45)
penup()
forward(10)
right(45)
pendown()
forward(35)
left(135)
penup()
forward(10)
left(45)
pendown()
forward(15)

#Signo positivo.
penup()
forward(33)
left(90)
forward(105)
pendown()
forward(8)
backward(4)
left(90)
forward(4)
backward(8)
penup()
forward(4)
right(90)


#Signo negativo.
forward(54)
left(90)
pendown()
forward(4)
backward(8)


turtle.exitonclick()



