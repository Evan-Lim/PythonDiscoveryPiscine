#!/usr/bin/env python3

i = 0
while i <= 10:
	print("Table of ", i, ": ", sep = "", end = "")
	j = 0
	while j <= 9:
		print(i * j, end = " ")
		j += 1
	print(i * j)
	i += 1
