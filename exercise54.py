# This is where Exercise 5.4 goes
# Name: Brendan Gassler

def is_triangle(a, b, c):
	if a > b + c:
		print "No"
	elif b > a + c:
		print "No"
	elif c > a + b:
		print "No"
	else:
		print "Yes"

a  = raw_input('What length is the first leg?\n')
b  = raw_input('What length is the second leg?\n')
c  = raw_input('What length is the third leg?\n')

is_triangle(a, b, c)