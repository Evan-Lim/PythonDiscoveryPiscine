#!/usr/bin/env python3

import sys

def shrink(data):
	return data[:8]

def enlarge(data):
	i = len(data)
	while i <= 7:
		data = data + 'Z'
		i += 1
	return data

if len(sys.argv) >= 2:
	i = 0
	while i < len(sys.argv) - 1:
		if len(sys.argv[i + 1]) == 8:
			print(sys.argv[i + 1])
		elif len(sys.argv[i + 1]) > 8:
			print(shrink(sys.argv[i + 1]))
		else:
			print(enlarge(sys.argv[i + 1]))
		i += 1	
else:
	print("none")
