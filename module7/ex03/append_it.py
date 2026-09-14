#!/usr/bin/env python3

import sys
if len(sys.argv) >= 2:
	i = 1
	while i <= len(sys.argv) - 1:
		if sys.argv[i].find("ism", len(sys.argv[i]) - 4) == -1:
			print(sys.argv[i], "ism", sep="")
		i += 1
else:
	print("none")
