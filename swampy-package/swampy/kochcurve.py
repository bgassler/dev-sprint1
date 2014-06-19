#Koch Curve function from exercise 5.6
#Name:Brendan Gassler

import math

from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()				
bob.delay = 0

def koch(turtle, length):
	if length < 3:
		fd(turtle, length*5)
	else:
		koch(turtle, length/3.0)
		lt(turtle, 60)
		koch(turtle, length/3.0)
		rt(turtle, 120)
		koch(turtle, length/3.0)
		lt(turtle, 60)
		koch(turtle, length/3.0)


def snowflake(turtle, length):
	for i in range(3):
		koch(turtle, length)
		rt(turtle, 120)


snowflake(bob, 96)

wait_for_user()	