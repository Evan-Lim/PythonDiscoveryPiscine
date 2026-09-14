#!/usr/bin/env python3

def greetings(data=None):
	if data == None:
		print("Hello, noble stranger.")
	elif not isinstance(data, str):
		print("Error! It was not a name.")
	else:
		print("Hello, ", data, ".", sep="")


greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)		
