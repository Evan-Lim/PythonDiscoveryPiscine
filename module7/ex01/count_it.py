#!/usr/bin/env python3

import sys
if len(sys.argv) >= 2:
	print("parameters:", len(sys.argv) - 1)
	for i in range(len(sys.argv) - 1):
		print(sys.argv[i + 1], ": ", len(sys.argv[i + 1]), sep="")
else:
	print("none")
