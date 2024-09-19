import turtle
from turtle import Turtle
import math
from turtledemo.penrose import start

import numpy

def rectangle(t, w,h):
	"""Draws a rectangle
	parameters:
		turtle, width, height"""
	parallelogram(t,w,h,90)

def rhombus(t, size, angle):
	parallelogram(t,size,size,angle)

def parallelogram(t,w,h,angle):
	"""Draws a rhombus
	Parameters:
		turtle, width, height, angle of lower-left corner"""
	otherangle = (180-angle)
	for i in ((w,angle),(h,otherangle))*2:
		t.forward(i[0])
		t.left(i[1])
		print(i)

def draw_pie(t, radius, slices):
	angle = 360 / slices
	for i in range(slices):
		i = i
		isosceles(t, radius, angle)
		t.left(angle)

def isosceles(t, length, angle):
	a0 = angle
	l0 = length
	a1 = (180-a0)/2.0
	l2 = 2*l0*math.tan(numpy.deg2rad(a0/2.0))
	l1 = math.sqrt((l2/2.0)**2 + l0**2)

	t.right(angle/2.0)
	for i in ((a1,l1),(a1,l2),(a0/2.0,l1)):
		t.forward(i[1])
		t.left(180-i[0])

def polyline(t, n,length,angle):
	for i in range(n):
		t.forward(length)
		t.left(angle)


def arc(t, radius, angle):
	arc_length = 2*math.pi*radius*math.fabs(angle)/360
	n = 20
	step_length = arc_length / n
	step_angle = angle / n
	origin = t.pos()
#	t.penup()
	polyline(t, n,step_length,step_angle)
#
#	offset = t.pos()-origin
#	t.left(math.degrees(math.atan(offset[0]/offset[1])))
	#t.pendown()
#	polyline(t, n, step_length, step_angle)

def draw_flower(t, radius, slices, completion):
	angle = 360 / slices
	for i in range(slices):
		petal(t, radius, completion)
		t.left(angle)

def petal(t,radius,angle):
	start_heading = t.heading()
	print(start_heading)
	t.right(angle/2.0)
	origin = t.pos()
	t.pendown()
	arc(t,radius,angle)
	t.right(180+angle)
	arc(t, radius, angle)
	t.setheading(start_heading)

t = turtle.Turtle()
t.speed(500)
t.pendown()
#arc(t, 100, 90)

#polyline(t,4,100,90)
#petal(t,100,45)
#rectangle(t, 100,100)
#isosceles(t, 100, 45)
#isosceles(t, 200, 90)
#arc(t, 100,90)
draw_flower(t,200,50, 90)

turtle.exitonclick()