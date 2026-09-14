#!/usr/bin/env python3

import sys
if len(sys.argv) == 3:
	if int(sys.argv[1]) < int(sys.argv[2]):
		arr = []
		for i in range(int(sys.argv[1]), int(sys.argv[2])):
			arr.append(i)
		arr.append(int(sys.argv[2]))
		print(arr)
else:
	print("none")
